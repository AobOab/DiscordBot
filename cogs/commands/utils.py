# Imports
import discord
import random
import string
from discord.ext import commands
from discord.commands import slash_command, Option

# Cog
class utils(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Ping
	@slash_command(description="Check the latency of the bot")
	async def ping(self, ctx):
		embed = discord.Embed(
			title = ":ping_pong: Pong!",
			description = f"The latency of the bot is **{round(self.bot.latency, 1)}**ms!",
			color = 0x2ecc71
		)
		embed.set_thumbnail(url='https://cdn3.emoji.gg/emojis/7916-verify-green.gif')
		await ctx.respond(embed=embed, ephemeral=True)

		
	# User Info
	@slash_command(description="Get Info of a user")
	async def userinfo(self, ctx, user: Option(discord.Member, "User", required=False)):
		user = user or ctx.author
		embed = discord.Embed(title = user, color = user.colour)
		embed.set_thumbnail(url=user.avatar.url)
		embed.add_field(name='User ID:', value = user.id)
		embed.add_field(name='Joined Discord on:', value = user.created_at.strftime("%b %d, %Y"))
		await ctx.respond(embed=embed)

		
	# Purge Channel
	@slash_command(description="Clear a channel's messages")
	async def purge(self, ctx, limit: Option(int, "Messages to delete")):
		if not ctx.author.guild_permissions.manage_messages:
			ctx.respond("You don't have permission to do that!", ephemeral=True)
		else:
			await ctx.channel.purge(limit=limit)
			await ctx.respond(f'Messages cleared by {ctx.author.mention}', delete_after=3)

			
	# Profile Pic
	@slash_command(description="Get a user's profile picture")
	async def pfp(self, ctx, user: Option(discord.Member, "User", required=False)):
		user = user or ctx.author
		embed = discord.Embed(title=f"{user}'s Profile Picture'")
		embed.set_image(url=user.avatar.url)
		await ctx.respond(embed=embed)

		
	#Password Generator (Max: 94 Characters)
	@slash_command(description="Generate a random password and send it through your dm")
	async def password(self, ctx, length: Option(int, "Password Length (94 Characters Maximum)")):
		lower = string.ascii_lowercase
		upper = string.ascii_uppercase
		num = string.digits
		symbols = string.punctuation

		all = lower + upper + num + symbols
	
		temp = random.sample(all, length)
		password = ".".join(temp)
		embed = discord.Embed(
			title = ":closed_lock_with_key: Password was sent through your dm!",
			color = 0x2ecc71
		)
		embed1 = discord.Embed(
			title = f":key: {password}",
			description = '(This message will be deleted after 1 minute)',
			color = 0x2ecc71
		)
		await ctx.respond(embed=embed)
		await ctx.author.send(embed=embed1, delete_after=60)
		

# Setup Function
def setup(bot):
	bot.add_cog(utils(bot))