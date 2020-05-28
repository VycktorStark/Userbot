from asyncio import sleep
import lang
async def Function(cmd, event, delt, LANG):
	try:
		message = await event.reply(lang.LANG['waitrules'])
	except Exception:
		await event.delete()
		raise StopPropagation
	finally:
		await sleep(5)
		msg = await message.edit(lang.LANG['rules'])
		await delt(event, msg, 900)
plugin = {
	'patterns': [
		'^[!|/]([r|R][u|U][l|L][e|E][s|S])$',
	],
	'function': Function,
	'sudo': False,
	'group': True,
	'private': False,
	}
