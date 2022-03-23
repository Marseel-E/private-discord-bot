from discord.ext.commands import Bot, when_mentioned_or
from discord import Intents, Status, Game
from os import listdir, environ
from dotenv import load_dotenv

from utils import Config, Default


class Bodyguard(Bot):
	def __init__(self):
		super().__init__(command_prefix=when_mentioned_or(Config.prefix), case_sensitive=True, intents=Intents.all(), application_id=environ.get("APP_ID"))


	async def on_ready(self):
		await self.change_presence(status=Status.online, activity=Game(Config.status))
		print("running")


	async def setup_hook(self):
		for file in listdir("cogs"):
			if file.endswith(".py"):
				try: await self.load_extension(f"cogs.{file[:-3]}")
				except Exception as e: print('\n', f"ERROR: failed to load '{file[:-3]}':\n", e, '\n')
				else: print(f"INFO: loaded '{file[:-3]}'")

		try:
			await self.tree.sync()
			await self.tree.sync(guild=Default.test_server)
		except Exception as e: print('\n', f"ERROR: faild to sync commands:\n", e, '\n')


if __name__ == '__main__':
	load_dotenv('.env')

	bot = Bodyguard()
	bot.run(environ.get("TOKEN"))