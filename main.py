#-*-coding:utf8;-*
from telethon import events
import random, time, logging, plugins, re
from lang import LANG
from asyncio import sleep
from tools import client, delt, sudo_id, chat_group_main
plugins_ = plugins.plugins_
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(levelname)s : %(message)s', datefmt='%H:%M:%S')

@client.on(events.ChatAction)
async def handler(event):
	if (event.user_joined):
		chat, user = await event.get_chat(), await event.get_user()
		if (chat.title == chat_group_main):
			await event.respond(LANG['welcome'].format(name=user.first_name), parse_mode='md')

@client.on(events.NewMessage)
async def info(event):
	try:
		chat, sender = await event.get_chat(), await event.get_sender()
		first_name, chat_id, sender_id = sender.first_name, event.chat_id, event.sender_id
		if ("Channel" in str(chat)): title, typ = chat.title, "Grupo"
		else: title, typ = chat.first_name, "Privado"
	except Exception:
		typ = "Canal"
		title = first_name = chat.title
		chat_id = sender_id = event.chat_id
	finally:
		logging.info(f"[{typ}] - {title} ({chat_id}):\n[{sender_id}] - {first_name} - Enviou: {event.raw_text}")
		await sleep(0.5)
	if (first_name == "falademais"):
		await event.delete()
	elif (event.raw_text):
		if (title == chat_group_main) or (typ == 'Privado') or (sender_id == sudo_id):
			for aPlugin in plugins_():
				for patterns in aPlugin['patterns']:
					cmd = re.search(patterns, event.raw_text, re.IGNORECASE)
					if not (cmd == None):
						if cmd.groups(): cmd = cmd.groups()
						else: cmd = cmd.group()
						try:
							if (aPlugin['sudo'] == True):
								if (event.sender_id == sudo_id):
									await aPlugin['function'](cmd, event, delt, LANG)
								else:
									await event.reply(LANG['notsudo'])
							elif (aPlugin['sudo'] == False):
								if (aPlugin['group'] == True) and (typ == "Grupo"):
									await aPlugin['function'](cmd, event, delt, LANG)
								elif (aPlugin['private'] == True) and (typ == "Privado"):
									await aPlugin['function'](cmd, event, delt, LANG)
						except Exception as error:
							print(error)

if __name__ == "__main__":
	client.start()
	client.run_until_disconnected()
