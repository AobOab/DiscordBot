# Imports
import discord
import requests
import json
from discord.ext import commands
from discord.commands import slash_command, Option

# Cog
class fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Quote
	@slash_command(description='Tells you a random quote.')
	async def quote(self, ctx):
		response = requests.get("https://zenquotes.io/api/random")
		json_data = json.loads(response.text)
		embed = discord.Embed(
			title = json_data[0]['q'],
			description = f"-{json_data[0]['a']}",
			color = 0x2ecc71
		)
		await ctx.respond(embed=embed)

# Setup Function
def setup(bot):
	bot.add_cog(fun(bot))