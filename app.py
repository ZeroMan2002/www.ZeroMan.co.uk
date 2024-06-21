# app.py
import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Fetch environment variables for Discord bot integration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

# Ensure CHANNEL_ID is an integer if needed for bot.get_channel()
try:
    CHANNEL_ID = int(CHANNEL_ID)
except ValueError:
    raise ValueError("CHANNEL_ID must be a valid integer")

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    
    payload = {
        "content": f"New submission:\nUsername: {username}\nEmail: {email}"
    }

    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages", json=payload, headers=headers)

    if response.status_code == 200:
        return "Success", 200
    else:
        return "Failed to send message to Discord", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
