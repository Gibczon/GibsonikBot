import os
import discord
from discord.ext import commands
import requests
import json
from keep_alive import keep_alive

client = commands.Bot(command_prefix = ".")



@client.event
async def on_ready():
  print("{0.user}".format(client) + " ready for action!")

inital_extension = []

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    inital_extension.append("cogs." +filename[:-3])

if __name__ == '__main__':
  for extension in inital_extension:
    client.load_extension(extension)

keep_alive()
client.run(os.environ['password'])
