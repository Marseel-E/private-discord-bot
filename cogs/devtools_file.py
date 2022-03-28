import os

from discord.app_commands import Group, command, check
from discord import Interaction, TextStyle
from discord.ext.commands import Cog, Bot
from discord.ui import Modal, TextInput

from utils import Default, is_owner


async def create_and_write(interaction: Interaction, name: str, content: str) -> None:
	FILE_PATH = f'dev_files/{name}'

	if not (content):
		await interaction.response.send_message(":x: Cannot create an empty file", ephemeral=True)
		return

	with open(FILE_PATH, 'w+') as f:
		f.write(content)

	await interaction.response.send_message(f":white_check_mark: Written `{os.path.getsize(FILE_PATH)}` bytes to '{self.name}'", ephemeral=True)

def get_file_content(name: str) -> str:
	with open(f'dev_files/{name}', 'r') as f:
		return f.read()


class Create_file(Modal):
	def __init__(self, file_name: str) -> None:
		self.file_name = file_name
		
		super().__init__(title="Create file", timeout=300.0)

		self.add_item(TextInput(label=f"{self.file_name} <NEW>", style=TextStyle.paragraph, placeholder="File content"))

	async def on_submit(self, interaction: Interaction):
		await create_and_write(interaction, self.file_name, self.children[0].value)


class Edit_file(Modal):
	def __init__(self, file_name: str) -> None:
		self.file_name = file_name
		
		super().__init__(title="Edit file", timeout=300.0)

		self.add_item(TextInput(label=f"{self.file_name}", style=TextStyle.paragraph, placeholder="File content", default=get_file_content(self.file_name)))

	async def on_submit(self, interaction: Interaction):
		await create_and_write(interaction, self.file_name, self.children[0].value)


class File(Cog, Group, name="file"):
	def __init__(self, bot: Bot) -> None:
		self.bot = bot
		super().__init__()

	async def interaction_check(self, interaction: Interaction) -> bool:
		return await is_owner(interaction)


	@command()
	async def create(self, interaction: Interaction, name: str, content: str = None):
		if not (content):
			await interaction.response.send_modal(Create_file(name))
			return

		await create_and_write(interaction, name, content)


	@command()
	async def flush(self, interaction: Interaction):
		for file in os.listdir('dev_files'):
			os.remove("dev_files/" + file)

		status = ":x:"
		if len(os.listdir('dev_files')) == 0: status = ":white_check_mark:"

		await interaction.response.send_message(status, ephemeral=True)


	@command()
	async def edit(self, interaction: Interaction, name: str, new_content: str = None):
		if not (new_content):
			await interaction.response.send_modal(Edit_file(name))
			return

		await create_and_write(interaction, name, new_content)


async def setup(bot: Bot):
	await bot.add_cog(File(bot), guilds=[Default.test_server])
