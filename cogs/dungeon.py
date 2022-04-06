from discord.ext.commands import Cog, Bot
from discord.app_commands import command, check, Range 
from discord import Interaction as Inter, embed

from utils import is_owner, Dungeon, Default


class Dungeon_slash(Cog):
	def __init__(self, bot: Bot) -> None:
		self.bot = bot


	@command()
	@check(is_owner)
	async def dungeon(self, inter: Inter, rows: Range[int, 5, 100] = 10, columns: Range[int, 5, 100] = 10):
		game = Dungeon(rows, columns)

		embed = Embed(title="Dungeon", description="", color=Default.color)

		for row in range(rows):
			for col in range(columns):
				embed.description += game.tiles[row][col].icon

		await inter.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: Bot) -> None:
	await bot.add_cog(Dungeon_slash(bot), guilds=[Default.test_server])