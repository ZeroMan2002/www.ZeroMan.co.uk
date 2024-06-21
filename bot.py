# bot.py
import os
from flask import Flask, request
import discord
from discord.ext import commands # type: ignore

app = Flask(__name__)

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

bot = commands.Bot(command_prefix='!')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        bot.loop.create_task(channel.send(f"New submission:\nUsername: {username}\nEmail: {email}"))
    
    return "Success", 200

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

if __name__ == "__main__":
    from threading import Thread
    def run_bot():
        bot.run(DISCORD_TOKEN)
    
    Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=5000)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Bot is now online!")
