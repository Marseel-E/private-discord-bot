from discord.ext.commands import Cog, Bot
from discord.app_commands import command, check, Range 
from discord import Interaction as Inter, Embed, ButtonStyle
from discord.ui import View, Button, button

from utils import is_owner, Dungeon, Default


class Controls(View):
	def __init__(self, inter: Inter, game) -> None:
		self._inter = inter
		self.game = game
		super().__init__(timeout=120.0)

	async def interaction_check(self, inter: Inter) -> bool:
		return (inter.user.id == self._inter.user.id)

	async def on_timeout(self) -> None:
		for item in self.children:
			item.disabled = True

		await self._inter.edit_original_message(view=self)


	@button(label="UP", style=ButtonStyle.green, row=0)
	async def up(self, inter: Inter, button: Button):
		pass

	@button(label="DOWN", style=ButtonStyle.green, row=0)
	async def down(self, inter: Inter, button: Button):
		pass

	@button(label="LEFT", style=ButtonStyle.green, row=1)
	async def left(self, inter: Inter, button: Button):
		pass

	@button(label="RIGHT", style=ButtonStyle.green, row=1)
	async def right(self, inter: Inter, button: Button):
		pass


class Dungeon_slash(Cog):
	def __init__(self, bot: Bot) -> None:
		self.bot = bot


	@command()
	@check(is_owner)
	async def dungeon(self, inter: Inter, rows: Range[int, 5, 20] = 10, columns: Range[int, 5, 20] = 10):
		game = Dungeon(inter.user.id, rows, columns)

		embed = Embed(title="Dungeon", description="", color=Default.color)

		for row in range(rows):
			embed.description += "\n"
			for col in range(columns):
				embed.description += game.tiles[row][col].icon

		view = Controls(inter, game)
		await inter.response.send_message(embed=embed, view=view)
		await view.wait()


async def setup(bot: Bot) -> None:
	await bot.add_cog(Dungeon_slash(bot), guilds=[Default.test_server])