	# Imports
import discord
from discord.ext import commands
from discord.commands import slash_command, Option

# Cog
class cog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

# Setup Function
def setup(bot):
	bot.add_cog(cog(bot))