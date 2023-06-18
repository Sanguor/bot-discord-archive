import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

description = '''A Discord bot that extracts data from server channels, fine-tunes a language model, and provides an archive for easy retrieval of old information.'''

load_dotenv()
TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Remove the import of the "commands" module if it exists
bot.remove_command('ping')
bot.remove_command('add')

# Import the commands from the new files
from commands.ping import ping
from commands.add import add

# Add the commands to the bot
bot.add_command(ping)
bot.add_command(add)


bot.run(TOKEN)