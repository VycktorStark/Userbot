import time
async def Function(cmd, event, delt, LANG):
	s = time.time()
	message = await event.reply("Pong!")
	d = time.time() - s
	msg = await message.edit(f'Pong! __(response led {d:.2f}s)__')
	await delt(event, msg, 8)
plugin = {
	'patterns': [
		'^[!|/]([p|P][i|I][n|N][g|G])$'
	],
	'function': Function,
	'sudo': False,
	'group': True,
	'private': True,
	}
