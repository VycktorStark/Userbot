from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from tools import client, isadmin
import lang
lang = lang.LANG['plugins']
banned_rights = ChatBannedRights(until_date=None,view_messages=True,send_messages=True)
unbanned_rights = ChatBannedRights(until_date=None,view_messages=None,send_messages=None)

async def Function(cmd, event, delt, LANG):
	reply = await event.get_reply_message()
	result = await client(GetParticipantRequest(event.chat_id, event.message.from_id))
	if isadmin(result) == True:
		if (cmd[0].lower() == 'ban'):
			if not (reply):
				if len(cmd) == 2:
					try:
						await client(EditBannedRequest(event.chat_id, cmd[1], banned_rights))
						await event.respond(lang['ban'])
					except Exception as error:
						await event.respond(lang['notarg'])
				else:
					await event.respond(lang['notreply'])
			else:
				await client(EditBannedRequest(event.chat_id, reply.from_id, banned_rights))
				await event.respond(lang['ban'])
		elif (cmd[0].lower() == 'unban'):
			if not (reply):
				if len(cmd) == 2:
					try:
						await client(EditBannedRequest(event.chat_id, cmd[1], unbanned_rights))
						await event.respond(lang['unban'])
					except Exception as error:
						await event.respond(lang['notarg'])
				else:
					await event.respond(lang['notreply'])
			else:
				await client(EditBannedRequest(event.chat_id, reply.from_id, unbanned_rights))
				await event.respond(lang['unban'])
plugin = {
	'patterns': [
		'^[!|/]([b|B][a|A][n|N])$',
		'^[!|/]([b|B][a|A][n|N]) (.+)$',
		'^[!|/]([u|U][n|N][b|B][a|A][n|N])$',
		'^[!|/]([u|U][n|N][b|B][a|A][n|N]) (.+)$',
	],
	'function': Function,
	'sudo': False,
	'group': True,
	'private': False,
	}
