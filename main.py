import os

from discord.ext.commands import Bot, command, when_mentioned_or
from discord import Intents, Status, Game, Object, Interaction
from discord.app_commands import commandTree
from dotenv import load_dotenv

from utils import Config

load_dotenv('.env')

bot = Bot(command_prefix=when_mentioned_or(Config.prefix), intents=Intents.all())
slashes = commandTree(bot)


@slashes.command(guild=Object(id=843994109366501376))
async def test_slash(interaction: Interaction, msg: str = None):
	await interaction.response.send_message(msg or "Worked", ephemeral=True)


@bot.event
async def on_ready():
	print("running")
	await bot.change_presence(status=Status.online, activity=Game(Config.status))


if __name__ == '__main__':
	for file in os.listdir('cogs'):
		if (file.endswith(".py")):
			try: bot.load_extension(f"cogs.{file[:-3]}")
			except Exception as e: print('\n', f"ERROR: failed to load '{file[:-3]}':\n", e, '\n')
			else: print(f"INFO: loaded '{file[:-3]}'")


bot.run(os.environ.get("TOKEN"))
