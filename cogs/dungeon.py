from discord.ext.commands import Cog, Bot
from discord.app_commands import command, check, Range 
from discord import Interaction as Inter, Embed, ButtonStyle
from discord.ui import View, Button, button
from typing import Tuple

from utils import is_owner, Dungeon, Default, Path


win_embed = Embed(title="Dungeon", description=":tada: You win! :tada:", color=Default.color)


async def style_dungeon_embed(rows: int, embed: Embed, columns: int, game: Dungeon) -> None:
	for row in range(rows):
		embed.description += "\n"
		for col in range(columns):
			embed.description += game.tiles[row][col].icon


class Controls(View):
	def __init__(self, inter: Inter, game: Dungeon, embed: Embed) -> None:
		self._inter = inter
		self.game = game
		self.embed = embed
		super().__init__(timeout=120.0)

	async def interaction_check(self, inter: Inter) -> bool:
		return (inter.user.id == self._inter.user.id)

	async def on_timeout(self) -> None:
		if (self.children):
			for item in self.children:
				item.disabled = True

			await self._inter.edit_original_message(view=self)


	def get_player(self) -> Tuple(int):
		for x in range(self.game.rows):
			for y in range(self.game.cols):
				if self.game.tiles[x][y].type == "player":
					return (x, y)


	@button(label="🔼", style=ButtonStyle.green, row=0)
	async def up(self, inter: Inter, button: Button):
		x, y = self.get_player()

		if x > 0:
			if self.game.tiles[x-1][y].type == "path":
				self.game.tiles[x][y] = Path()
				self.game.tiles[x-1][y] = self.game.player

				await style_dungeon_embed(self.game.rows, self.embed, self.game.cols, self.game)

			if self.game.tiles[x-1][y].type == "door":
				e_x, e_y = self.game.end
				if (x-1 == e_x) and (y == e_y):
					await self._inter.edit_original_message(embed=win_embed, view=self)
					self.stop()

	@button(label="🔽", style=ButtonStyle.green, row=0)
	async def down(self, inter: Inter, button: Button):
		x, y = self.get_player()

		if x < (self.game.rows - 1):
			if self.game.tiles[x+1][y].type == "path":
				self.game.tiles[x][y] = Path()
				self.game.tiles[x+1][y] = self.game.player

				await style_dungeon_embed(self.game.rows, self.embed, self.game.cols, self.game)

			if self.game.tiles[x+1][y].type == "door":
				e_x, e_y = self.game.end
				if (x+1 == e_x) and (y == e_y):
					await self._inter.edit_original_message(embed=win_embed, view=self)
					self.stop()

	@button(label="◀", style=ButtonStyle.green, row=1)
	async def left(self, inter: Inter, button: Button):
		x, y = self.get_player()

		if y > 0:
			if self.game.tiles[x][y-1].type == "path":
				self.game.tiles[x][y] = Path()
				self.game.tiles[x][y-1] = self.game.player

				await style_dungeon_embed(self.game.rows, self.embed, self.game.cols, self.game)

			if self.game.tiles[x][y-1].type == "door":
				e_x, e_y = self.game.end
				if (x == e_x) and (y-1 == e_y):
					await self._inter.edit_original_message(embed=win_embed, view=self)
					self.stop()

	@button(label="▶", style=ButtonStyle.green, row=1)
	async def right(self, inter: Inter, button: Button):
		x, y = self.get_player()
		print("INFO: player", x, y)

		if y < (self.game.cols - 1):
			print("INFO: index check passed")

			if self.game.tiles[x][y+1].type == "path":
				print("INFO: found path")

				self.game.tiles[x][y] = Path()
				print("INFO: replaced player with path")
				self.game.tiles[x][y+1] = self.game.player
				print("INFO: replaced (x, y+1) with player", x, y+1)

				await style_dungeon_embed(self.game.rows, self.embed, self.game.cols, self.game)
				print("INFO: styled embed")

			if self.game.tiles[x][y+1].type == "door":
				print("INFO: found door")

				e_x, e_y = self.game.end
				print("INFO: end coordinates", e_x, e_y)
				if (x == e_x) and (y+1 == e_y):
					print("INFO: passed index check")
					self.embed = win_embed
					print("INFO: replaced embed with win embed")
					for item in self.children:
						await self.remove_item(item)
					print("INFO: removed view items")

		await self._inter.edit_original_message(embed=self.embed, view=self)
		print("INFO: edited msg")


class Dungeon_slash(Cog):
	def __init__(self, bot: Bot) -> None:
		self.bot = bot


	@command()
	@check(is_owner)
	async def dungeon(self, inter: Inter, rows: Range[int, 5, 20] = 10, columns: Range[int, 5, 20] = 10):
		game = Dungeon(inter.user.id, rows, columns)

		embed = Embed(title="Dungeon", description="", color=Default.color)

		await style_dungeon_embed(rows, embed, columns, game)

		view = Controls(inter, game, embed)
		await inter.response.send_message(embed=embed, view=view)
		await view.wait()


async def setup(bot: Bot) -> None:
	await bot.add_cog(Dungeon_slash(bot), guilds=[Default.test_server])