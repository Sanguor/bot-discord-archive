# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

description = '''A Discord bot that extracts data from server channels, fine-tunes a language model, and provides an archive for easy retrieval of old information.'''

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    """Checks if bot is alive."""
    await ctx.send('pong!')

@bot.command(name='add')
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run(TOKEN)