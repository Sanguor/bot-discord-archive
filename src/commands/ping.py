from discord.ext import commands

@commands.command()
async def ping(ctx):
    """Checks if bot is alive."""
    await ctx.send('pong!')

def setup(bot):
    bot.add_command(ping)
