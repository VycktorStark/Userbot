from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
from telethon import TelegramClient, events
from asyncio import sleep
import time, logging, subprocess, os
client = TelegramClient('cwf',api_id=os.environ['APIKEYHASID'] ,api_hash=os.environ['APIKEYHAS'])
sudo_id = 438131290
chat_group_main = "NameYourChatGroup"
def bash_(self):
	try:
		resp = subprocess.check_output(self, shell=True).decode('utf8')
		if (len(resp) == 1) and (resp == "\n"):
			resp = "OK"
		return resp
	except Exception as error:
		logging.warning(error)
		return error
def isadmin(self):
	if isinstance(self.participant, ChannelParticipantCreator) == True:
		return True
	elif isinstance(self.participant, ChannelParticipantAdmin) == True:
		return True
	else:
		return False

async def delt(even, item, sleep_):
	await sleep(sleep_)
	if (even): await even.delete()
	if (item): await item.delete()

__all__ = ['client', 'delt', 'sudo_id', 'sleep', 'isadmin']
