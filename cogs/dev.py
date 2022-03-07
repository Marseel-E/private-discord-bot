import traceback
import json
import sys
import os

from discord.ext.commands import Cog, command, is_owner, Context
from discord import Embed, User
from typing import Optional
from io import StringIO

from utils import Default, Config


class Dev(Cog):
	def __init__(self, bot):
		self.bot = bot

	async def cog_check(self, ctx: Context) -> bool:
		return (await self.bot.is_owner(ctx.author))


	@command(aliases=['ua'])
	async def update_avatar(self, ctx: Context, new_avatar: Optional[bool] = False):
		""" Updates the bot's avatar. 

		Parameters:
		-----------
			new_avatar <bool> - Whether to use a custom avatar or not.
		"""
		await ctx.message.delete()

		with open(Config.logo_path, 'rb') as img:
			avatar = img.read()

		await self.bot.user.edit(avatar=avatar)

		await ctx.send("Updated", delete_after=5)


	@command(aliases=['uu'])
	async def update_username(self, ctx: Context, new_username: str = ""):
		""" Updates the bot's username.

		Parameters:
		-----------
			new_username <str> - The new username.
		"""
		await ctx.message.delete()

		if not (new_username): await ctx.send("You need to pass a username", delete_after=5); return

		await self.bot.user.edit(username=new_username)

		await ctx.send("updated", delete_after=5)


	@command(aliases=['dm'])
	async def direct_message(self, ctx: Context, member: User, message: str, embeded: Optional[bool] = False):
		""" Sends a direct message to the specified member.

		Parameters:
		-----------
			member <discord.User> - The member to send the message to. (Required)
			message <str> - The message to send to the user. (Required)
			
			embeded <bool> - Whether to send an embed or not.
		"""
		await ctx.message.delete()

		kwargs = {'content': f"{message}\n\nSupport Server: <{Default.support_server_link}>"} if not (embeded) else {'embed': Embed(title="RPGBruh", description=f"{message}\n\n{Default.support_server}")}

		await member.send(**kwargs)


	@command(aliases=['python', 'py'])
	async def eval(self, ctx: Context, unformatted: Optional[bool], *, cmd: str):
		""" Evaluates python code

		Parameters:
		-----------
			cmd <str> - The ccode to evalutae. (Required)

			unformatted <bool> - Whether to send the text in a styalized embed or not.
		"""
		try: await ctx.message.delete()
		except: pass

		old_stdout = sys.stdout
		redirected_output = sys.stdout = StringIO()
		
		try: exec(str(cmd))
		except Exception as e:
			traceback.print_stack(file=sys.stdout)
			print(sys.exc_info())

		sys.stdout = old_stdout
		
		if (unformatted):
			msg = str(redirected_output.getvalue())
			msg = [await ctx.send(msg[i:i+2000]) for i in range(0, len(msg), 2000)]
		
		else:
			msg = str(redirected_output.getvalue())
			
			for i in range(0, len(msg), 2048):

				embed = Embed(description=f"Input:\n```py\n{cmd}\n```\nOutput:\n```bash\n{msg[i:i+2000]}\n```", color=Default.color)
				await ctx.send(embed=embed)


	@command()
	async def load(self, ctx: Context, cog: Optional[str] = None):
		""" Loads a cog.

		Parameters:
		-----------
			cog <str> - The cog name.
		"""
		if not (cog):
			for cog in os.listdir("cogs"):
				if not (cog.endswith(".py")) or (cog.startswith("dev")): continue

				try: self.bot.load_extension(f"cogs.{cog[:-3]}")
				except Exception as e: await ctx.author.send(f"[Main]: Failed to load '{cog[:-3]}': {e}")
				else: await ctx.send(f"[{cog[:-3]}]: Loaded..")

			return

		try: self.bot.load_extension(f"cogs.{cog}")
		except Exception as e: await ctx.author.send(f"[Main]: Failed to load '{cog}': {e}")
		else: await ctx.send(f"[{cog}]: Loaded..")

	@command()
	async def unload(self, ctx: Context, cog: Optional[str] = None):
		""" Unloads a cog.
		
		Parameters:
		-----------
			cog <str> - The cog name.
		"""
		if not (cog):
			for cog in os.listdir("cogs"):
				if not (cog.endswith(".py")) or (cog.startswith("dev")): continue

				try: self.bot.unload_extension(f"cogs.{cog[:-3]}")
				except Exception as e: await ctx.author.send(f"[Main]: Failed to unload '{cog[:-3]}': {e}")
				else: await ctx.send(f"[{cog[:-3]}]: Unloaded..")

			return

		try: self.bot.unload_extension(f"cogs.{cog}")
		except Exception as e: await ctx.author.send(f"[Main]: Failed to unload '{cog}': {e}")
		else: await ctx.send(f"[{cog}]: Unloaded..")

	@command()
	async def reload(self, ctx: Context, cog: Optional[str] = None):
		""" Reloads a cog.

		Parameters:
		-----------
			cog <str> - The cog name.
		"""
		if not (cog):
			for cog in os.listdir("cogs"):
				if not (cog.endswith(".py")): continue

				try: self.bot.reload_extension(f"cogs.{cog[:-3]}")
				except Exception as e: await ctx.author.send(f"[Main]: Failed to reload '{cog[:-3]}': {e}")
				else: await ctx.send(f"[{cog[:-3]}]: Reloaded..")

			return

		try: self.bot.reload_extension(f"cogs.{cog}")
		except Exception as e: await ctx.author.send(f"[Main]: Failed to reload '{cog}': {e}")
		else: await ctx.send(f"[{cog}]: Reloaded..")


def setup(bot):
	bot.add_cog(Dev(bot))
