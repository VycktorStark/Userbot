from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from tools import client
import lang
lang = lang.LANG['plugins']
muted_rights = ChatBannedRights(until_date=None,view_messages=None,send_messages=True)
unmuted_rights = ChatBannedRights(until_date=None,view_messages=None,send_messages=False)
async def Function(cmd, event, delt, LANG):
	reply = await event.get_reply_message()
	if (cmd[0].lower() == "mute"):
		if not (reply):
			if len(cmd) == 2:
				try:
					await client(EditBannedRequest(event.chat_id, cmd[1], muted_rights))
					await event.respond(lang['muteon'])
				except Exception as error:
					await event.respond(lang['notarg'])
			else:
				await event.respond(lang['notreply'])
		else:
			await client(EditBannedRequest(event.chat_id, reply.from_id, muted_rights))
			await event.respond(lang['muteon'])
	elif (cmd[0].lower() == "unmute"):
		if not (reply):
			if len(cmd) == 2:
				try:
					await client(EditBannedRequest(event.chat_id, cmd[1], unmuted_rights))
					await event.respond(lang['muteoff'])
				except Exception as error:
					await event.respond(lang['notarg'])
			else:
				await event.respond(lang['notreply'])
		else:
			await client(EditBannedRequest(event.chat_id, reply.from_id, unmuted_rights))
			await event.respond(lang['muteoff'])
plugin = {
	'patterns': [
		'^[!|/]([m|M][u|U][t|T][e|E])$',
		'^[!|/]([u|U][n|N][m|M][u|U][t|T][e|E])$',
		'^[!|/]([m|M][u|U][t|T][e|E]) (.+)$',
		'^[!|/]([u|U][n|N][m|M][u|U][t|T][e|E]) (.+)$',
	],
	'function': Function,
	'sudo': False,
	'group': True,
	'private': False,
	}
