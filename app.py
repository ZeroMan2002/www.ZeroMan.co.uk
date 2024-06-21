# app.py
import os
from flask import Flask, request
import requests

app = Flask(__name__)

DISCORD_BOT_URL = "https://discord.com/api/v10/channels/<CHANNEL_ID>/messages"  # Replace with your actual Discord channel URL

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    
    payload = {
        "content": f"New submission:\nUsername: {username}\nEmail: {email}"
    }

    headers = {
        "Authorization": f"Bot {os.getenv('DISCORD_TOKEN')}",
        "Content-Type": "application/json"
    }

    response = requests.post(DISCORD_BOT_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return "Success", 200
    else:
        return "Failed to send message to Discord", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
