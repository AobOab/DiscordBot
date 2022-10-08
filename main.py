# Imports
import os
import discord
from alive import keep_alive

# Variables
bot = discord.Bot(debug_guilds=[999657693063172156])

# Command Handlers
for commandfile in os.listdir('./cogs/commands'):
	if commandfile.endswith('.py'):
		bot.load_extension(f'cogs.commands.{commandfile[:-3]}')

# Event Handlers
for eventfile in os.listdir('./cogs/events'):
	if eventfile.endswith('.py'):
		bot.load_extension(f'cogs.events.{eventfile[:-3]}')

# Run
keep_alive()
bot.run(os.environ['token'], reconnect=True)