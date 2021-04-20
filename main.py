import os
import crayons
import discord
from discord.ext import commands

my_secret = os.environ['token']

client = commands.Bot(command_prefix='/');

@client.event 
async def on_ready():
  print(crayons.green(f'Bot is ready!'));

@client.command()
async def hello(ctx):
  await ctx.send('Hi!')


client.run('TOKEN') # use this if self hosting or something lmao
client.run(os.environ['token']); # use this if running in repl with secrets
