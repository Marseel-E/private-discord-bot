from discord import User, Member, Interaction, TextStyle, ButtonStyle
from discord.ui import Modal, TextInput, View, Button, button
from discord.ext.commands import Cog, command, is_owner, Context
from typing import Optional, Union


class Captcha(Modal, title="Verify your a human"):
	captcah = 'ABCDEFGH'
	answer = TextInput(label=captcah, style=TextStyle.short)

	async def on_submit(self, interaction: Interaction):
		msg = "Verified" if (self.answer == self.captcah) else "Your a robot"
		
		await interaction.response.send_message(msg, ephemeral=True)


class Captcha_view(View):
	def __init__(self, author: Union[Member, User]):
		super().__init__()
		self.author = author
		self.verified = False

	async def interaction_check(self, interaction: Interaction) -> bool:
		return False if (self.verified) else (interaction.user.id == self.author.id)


	@button(label="Verify", style=ButtonStyle.green)
	async def captcah_button(self, button: Button, interaction: Interaction):
		await interaction.response.send_modal(Captcha())
		self.stop()


class Join(Cog):
	def __init__(self, bot):
		self.bot = bot


	@Cog.listener(name="on_member_join")
	async def on_member_join(self, member: Member):
		channel = await self.bot.fetch_channel(846981584774103113)
		message = channel.last_message

		if (message.author.id == self.bot.user.id): await message.delete()

		view = Captcha_view(member)

		await channel.send("Verify your a human!", view=view)


	@command()
	@is_owner()
	async def test_join_message(self, ctx: Context, verify_message: Optional[str] = "Verify your a human!"):
		await ctx.message.delete()

		channel = await self.bot.fetch_channel(846981584774103113)
		message = channel.last_message

		if (message.author.id == self.bot.user.id): await message.delete()

		view = Captcha_view(ctx.author)

		await ctx.send(content=verify_message, view=view)


def setup(bot):
	bot.add_cog(Join(bot))