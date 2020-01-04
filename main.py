import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
  print ("Alice is ready")

client.run ('NjYyOTg0ODgxMDEzNTIyNDQ0.XhB7Rg.GQPD50VydAjZe0oxZw3BFtyub8M')

