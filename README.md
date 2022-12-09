# discorash.py
This module can be used to create crash bots

Это модуль для создания краш ботов

#Example


import discord
from discocrash import crashfuncs
from discord.ext import commands, tasks
import asyncio




intents = discord.Intents.all()
bot = commands.Bot(command_prefix="cr!", intents=intents)
bot.remove_command('help')
token = "token"


@bot.command()
async def crush(ctx):
	await crashfuncs.crash(ctx, "crashed", "crash", "crash", "crashed-by-janek", "crashed-by-janek", 10, 10)


bot.run(token)
