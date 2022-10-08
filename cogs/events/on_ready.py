# Imports
from discord.ext import commands

# Cog
class on_ready(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"Logged in as {self.bot.user}")

def setup(bot):
	bot.add_cog(on_ready(bot))