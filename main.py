from discord.ext.commands import Bot, command
from discord import Intents, Status, Game
from dotenv import load_dotenv
import os

load_dotenv('.env')

bot = Bot(command_prefix='.', intents=Intents.default())


@bot.event
async def on_ready():
	print("running")
	await bot.change_presence(status=Status.online, activity=Game("bodyguard.exe"))


if __name__ == '__main__':
	for file in os.listdir('cogs'):
		if (file.endswith(".py")):
			try: bot.load_extension(f"cogs.{file[:-3]}")
			except Exception as e: print('\n', f"ERROR: failed to load '{file[:-3]}':\n", e, '\n')
			else: print(f"INFO: loaded '{file[:-3]}'")


bot.run(os.environ.get("TOKEN"))