from telethon import TelegramClient, events
from asyncio import sleep
import time, logging, subprocess, os
client = TelegramClient('cwf',api_id=os.environ['APIKEYHASID'] ,api_hash=os.environ['APIKEYHAS'])
sudo_id = os.environ['YOURID']
chat_group_main = os.environ["GROUPSNAME"]
def bash_(self):
	try:
		resp = subprocess.check_output(self, shell=True).decode('utf8')
		if (len(resp) == 1) and (resp == "\n"):
			resp = "OK"
		return resp
	except Exception as error:
		logging.warning(error)
		return error

async def delt(even, item, sleep_):
	await sleep(sleep_)
	if (even): await even.delete()
	if (item): await item.delete()

__all__ = ['client', 'delt', 'sudo_id', 'sleep']
