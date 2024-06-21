import os
import discord
from discord.ext import commands

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        print(f'Connected to channel: {channel.name} (ID: {channel.id})')

@bot.command(name='force_online')
async def force_online(ctx):
    """Forces the bot to send an online message to the configured channel."""
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Force online command received. Bot is now online!")
    else:
        await ctx.send("Error: Channel not found. Check configuration.")

# Add more bot commands and event handlers here as needed

if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
