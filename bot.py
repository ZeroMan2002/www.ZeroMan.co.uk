# bot.py
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
        await channel.send("Bot is now online!")

# Run the bot
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
