from discord.ext import commands
import pandas as pd
import discord

def get_channel(ctx, channel_name):
    channel = discord.utils.get(ctx.guild.channels, name=channel_name)
    if channel is None:
        return "Channel not found."
    else:
        return channel

@commands.command()
async def scan(ctx):
    """Scans channel."""

    limit = 100
    df = pd.DataFrame(columns=['content', 'time', 'author'])

    # As an example, I've set the limit to 10000
    # meaning it'll read 10000 messages
    # instead of the default amount of 100

    target_channel = get_channel(ctx, '🍻taverne')

    async for msg in target_channel.history():
        new_row = {'content': msg.content,
                            'time': msg.created_at,
                            'author': msg.author.name}

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        if len(df) == limit:
            break

    file_location = "data.csv"  # Set the string to where you want the file to be saved to
    df.to_csv(file_location)


def setup(bot):
    bot.add_command(scan)
