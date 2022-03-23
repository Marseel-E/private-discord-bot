from discord.app_commands import command, guilds, check, Range
from discord.ext.commands import Cog
from discord import Interaction
from paginator import Paginator

from utils import Default, is_owner


class Test_cog(Cog):
	def __init__(self, bot):
		self.bot = bot


	@command()
	@guilds(Default.test_server)
	@check(is_owner)
	async def test_pagination(self, interaction: Interaction, pages_amount: int = 15, items_per_page: int = 5):
		pages = []; page_content = ""

		for i in range(pages_amount):
			if (i > 0) and (i % items_per_page == 0):
				pages.append(page_content)
				page_content = ""

			page_content += f"{i+1}. Item `{i}`\n"

		if (page_content != "") and not (page_content in pages): pages.append(page_content)

		await Paginator(interaction, pages).start()


async def setup(bot):
	await bot.add_cog(Test_cog(bot))