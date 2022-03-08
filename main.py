import os

from discord import Intents, Status, Game, Object, Interaction, Member
from discord.ext.commands import Bot, command, when_mentioned_or
from discord.app_commands import CommandTree
from dotenv import load_dotenv

from utils import Config

load_dotenv('.env')

bot = Bot(command_prefix=when_mentioned_or(Config.prefix), intents=Intents.all())
slashes = CommandTree(bot)
test_server = Object(id=843994109366501376)


@slashes.command(guild=test_server)
async def kick(interaction: Interaction, member: Member, reason: str = ""):
	assert (await bot.is_owner(interaction.user))

	try: await member.send(f"you got kicked by '{interaction.user}'" + (f" for {reason}" if (reason) else ""))
	except: pass

	await interaction.guild.kick(member, reason=reason)
	await interaction.response.send_message(f"kicked '{member}'", ephemeral=True)


@bot.event
async def on_ready():
	print("running")
	await slashes.sync(guild=test_server)
	await bot.change_presence(status=Status.online, activity=Game(Config.status))


if __name__ == '__main__':
	for file in os.listdir('cogs'):
		if (file.endswith(".py")):
			try: bot.load_extension(f"cogs.{file[:-3]}")
			except Exception as e: print('\n', f"ERROR: failed to load '{file[:-3]}':\n", e, '\n')
			else: print(f"INFO: loaded '{file[:-3]}'")

bot.run(os.environ.get("TOKEN"))
