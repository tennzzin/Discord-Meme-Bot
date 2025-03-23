import os
import discord
import requests
import json
from dotenv import load_dotenv

# Load environment variables from a .env file
# This keeps sensitive data like tokens safe and out of the code
load_dotenv()

# Function to get a random meme from the meme-api
def get_meme():
    response = requests.get('https://meme-api.com/gimme')  # Make a GET request to fetch meme data
    json_data = json.loads(response.text)  # Convert the response to JSON format

    return json_data['url']  # Return the URL of the meme image

# Creating a custom Discord client by extending discord.Client
class MyClient(discord.Client):
    # This function runs once when the bot has successfully connected
    async def on_ready(self):
        print('Logged in as {0}!'.format(self.user))  # Print bot's username to confirm it's running

    # This function handles incoming messages
    async def on_message(self, message):
        # Ignore messages sent by the bot itself to avoid infinite loops
        if message.author == self.user:
            return 
        
        # Check if the message starts with the command '$meme'
        if message.content.startswith('$meme'):
            # Send a random meme image URL back to the same channel
            await message.channel.send(get_meme())

# Setting up intents so the bot can read message content (needed for on_message to work)
intents = discord.Intents.default()
intents.message_content = True

# Create an instance of MyClient with the specified intents
client = MyClient(intents=intents)

# Run the bot using the token stored in the DISCORD_BOT_TOKEN environment variable
client.run(os.getenv('DISCORD_BOT_TOKEN'))
