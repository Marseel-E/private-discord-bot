import random

from discord import User, Member, Interaction, TextStyle, ButtonStyle, Message
from discord.ui import Modal, TextInput, View, Button, button
from discord.ext.commands import Cog, command, is_owner, Context
from typing import Optional, Union

from utils import Config


LIST_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class Captcha(Modal, title="Verify your a human"):
	captcah = ''.join(random.choices(LIST_CHARACTERS, k=6)).upper()
	answer = TextInput(label=f"Write the following '{captcah}'", style=TextStyle.short, placeholder="Captcha code", min_length=6, max_length=6)

	async def on_submit(self, interaction: Interaction):
		msg = "Verified" if (str(self.answer).upper() == self.captcah) else "Your a robot"
		
		await interaction.response.send_message(msg, ephemeral=True)


class Captcha_view(View):
	def __init__(self, author: Union[Member, User], message: Message):
		super().__init__()
		self.author = author
		self.message = message
		self.verified = False

	async def interaction_check(self, interaction: Interaction) -> bool:
		return False if (self.verified) else (interaction.user.id == self.author.id)

	async def on_timeout(self): await self.message.delete()


	@button(label="Verify", style=ButtonStyle.green)
	async def captcah_button(self, button: Button, interaction: Interaction):
		await interaction.response.send_modal(Captcha())
		
		self.stop()


class Join(Cog):
	def __init__(self, bot):
		self.bot = bot


	@Cog.listener(name="on_member_join")
	async def on_member_join(self, member: Member):
		""" Sends a message to the specified channel whenever a member joins with a specific view to them only for verification. """
		channel = await self.bot.fetch_channel(Config.join_channel)

		msg = await channel.send("Loading...")

		view = Captcha_view(member, msg)
		await msg.edit(f"{member.mention}, " + Config.verify_message, view=view)


	@command(aliases=['tv'])
	@is_owner()
	async def test_verify(self, ctx: Context):
		""" Sends a test message for the join message event. """
		await ctx.message.delete()

		msg = await ctx.send("Loading...")

		view = Captcha_view(ctx.author, msg)
		await msg.edit(f"{ctx.author.mention}, " + Config.verify_message, view=view)


def setup(bot):
	bot.add_cog(Join(bot))