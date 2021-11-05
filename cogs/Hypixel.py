import discord
from discord.ext import commands
import os
#import io
import requests
#import base64
#import nbt

print("Requesting hypixel bazaar API...")
bazaar = requests.get("https://api.hypixel.net/skyblock/bazaar?key=" + os.environ["hypixelAPIkey"]).json()

#def decode_base64_data(raw):
#  data = nbt.nbt.NBTFile(fileobj=io.BytesIO(base64.b64decode(raw)))
#  return data

class Hypixel(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def goldentooth(self, ctx):
    enchanted_gold = bazaar["products"]["ENCHANTED_GOLD"]["quick_status"]["sellPrice"]
    wolf_tooth = bazaar["products"]["WOLF_TOOTH"]["quick_status"]["sellPrice"]
    golden_tooth = bazaar["products"]["GOLDEN_TOOTH"]["quick_status"]["buyPrice"]
    profit = golden_tooth - (enchanted_gold*32 + wolf_tooth*128)
    await ctx.send("Enchanted gold price (1): " + str(enchanted_gold))
    await ctx.send("Wolf tooth price (1): " + str(wolf_tooth))
    await ctx.send("Spending: " + str((enchanted_gold*32 + wolf_tooth*128)) + " for profit value of: " + str(profit))

def setup(client):
  client.add_cog(Hypixel(client))
