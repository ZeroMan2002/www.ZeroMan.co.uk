# bot.py
import os
from flask import Flask, request
import discord
from discord.ext import commands

app = Flask(__name__)

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

intents = discord.Intents.default()  # Default intents
intents.message_content = True       # Enable message content intent (needed for reading messages)

bot = commands.Bot(command_prefix='!', intents=intents)

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
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Bot is now online!")

if __name__ == '__main__':
    # Use Gunicorn as the production server
    import multiprocessing
    workers = multiprocessing.cpu_count() * 2 + 1
    bind = '0.0.0.0:5000'
    reload = True if os.getenv('FLASK_ENV') == 'development' else False
    loglevel = 'debug' if os.getenv('FLASK_ENV') == 'development' else 'info'

    # Run Flask app with Gunicorn
    from gunicorn.app.base import BaseApplication

    class StandaloneApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key, value)

        def load(self):
            return self.application

    options = {
        'bind': bind,
        'workers': workers,
        'reload': reload,
        'loglevel': loglevel
    }

    StandaloneApplication(app, options).run()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Bot is now online!")
