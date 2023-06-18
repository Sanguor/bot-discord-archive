from discord.ext import commands

@commands.command(name='add')
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

def setup(bot):
    bot.add_command(add)
