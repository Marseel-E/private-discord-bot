from discord import Interaction, Object
from discord.app_commands import command, guilds
from discord.ext.commands import Cog


test_guild = Object(id=843994109366501376)

class Test_slash(Cog):
    def __init__(self, bot):
        self.bot = bot


    @command()
    @guilds(test_guild)
    async def test(self, interaction: Interaction):
        await interaction.response.send_message("works", ephemeral=True)


def setup(bot):
    bot.add_cog(Test_slash(bot))
