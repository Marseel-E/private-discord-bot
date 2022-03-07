from discord.ext.commands import Cog, command, is_owner, Context
from typing import Optional


class Dev(Cog):
	def __init__(self, bot):
		self.bot = bot


	@command()
	@is_owner()
	async def update_avatar(self, ctx: Context, new_avatar: Optional[bool] = False):
		await ctx.message.delete()

		with open("../logo.png", 'rb') as img:
			avatar = img.read()

		await self.bot.user.edit(avatar=avatar)

		await ctx.send("Updated", delete_after=5)


def setup(bot):
	bot.add_cog(Dev(bot))