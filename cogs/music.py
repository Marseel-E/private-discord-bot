import pafy

from discord.app_commands import Group, command, check
from discord import Interaction as Inter, Embed, ButtonStyle
from discord.ext.commands import Cog, Bot
from discord.ui import View, Button, button

from utils import Default, is_owner


testing_url = "https://youtu.be/HmP_wGYw1_g"


class Controls_view(view):
	def __init__(self, _inter: Inter) -> None:
		self._inter = _inter

		super().__init__()

	async def interaction_check(self, inter: Inter) -> bool:
		return (self._inter.user.id == inter.user.id)

	async def on_timeout(self) -> None:
		for item in self.children:
			self.item.disabled = True

		await self._inter.edit_original_message(view=view)


	@button(label="stop", style=ButtonStyle.red)
	async def stop(self, inter: Inter, button: Button) -> None:
		await self.on_timeout()
		self.stop()



class Music(Cog, Group, name="music"):
	def __init__(self, bot: Bot) -> None:
		self.bot = bot
		super().__init__()

	# for development
	async def interaction_check(self, inter: Inter) -> bool:
		return await is_owner(inter)


	@command()
	async def play(self, inter: Inter, url: str = testing_url) -> None:
		videos = pafy.new(url).getbest()

		embed = Embed(
			title=f"{video.title } | {video.author}",
			description=video.description,
			color=Default.Color
		)
		embed.set_footer(text=f"Duration: {video.duration}")

		view = Controls_view(inter)
		await inter.response.send_message(embed=embed, ephemeral=True, view)
		await view.wait()


async def setup(bot: Bot):
	await bot.add_cog(Music(bot), guilds=[Default.test_server])