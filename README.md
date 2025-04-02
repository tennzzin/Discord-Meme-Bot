# Discord Meme Bot 🤖

## Overview

The Discord Meme Bot is a simple, beginner-friendly Python bot that fetches and sends random memes to a Discord channel using the Meme API. Built using the `discord.py` library, this bot responds to a custom command and serves as a great starter project for learning how to work with APIs, bots, and environment variables.

## Features
- **Random Meme Command**: Type `$meme` in any channel where the bot is present to receive a fresh meme from Reddit.
- **API Integration**: Connects to [meme-api.com](https://meme-api.com/) to fetch meme content in real-time.
- **Secure Token Handling**: Uses `.env` files and environment variables to protect your bot token.
- **Basic Event Handling**: Handles `on_ready()` and `on_message()` events using `discord.Client`.

## How to Use
1. Clone the Repository:
   - `git clone https://github.com/yourusername/discord-meme-bot.git`
   - `cd discord-meme-bot`
2. Set Up Virtual Environment:
   - Create a virtual environment
   - `python3 -m venv venv` 
   - Activate the virtual environment
   `source venv/bin/activate`  # On Mac/Linux
3. Install Dependecies:  
   - `pip install discord.py python-dotenv requests`
4. Set Up Environment:
   - Create a .env file in the root directory:
   - `DISCORD_BOT_TOKEN=your_bot_token_here`
5. Run the Bot:  
   - `python bot.py`
6. Test It:
   - Go to your Discord server and type:  
      `$meme`
   - The bot should reply with a meme image URL!

## Technology Stack
- **Lanuage**: Python
- **Libraries**:
  - `discord.py` – for interacting with the Discord API
  - `requests` – to call the meme API
  - `python-dotenv` – for loading environment variables
- **External API**: [Meme API](https://meme-api.com/)

## Skills Demonstrated

- **API Consumption**  
  Integrated a third-party meme API using HTTP requests.

- **Bot Development**  
  Built and deployed a functional Discord bot with message handlers.

- **Security Practices**  
  Used `.env` and `.gitignore` to protect sensitive information (like your bot token).

- **Event-Driven Programming**  
  Responded to Discord events such as bot readiness and incoming messages.

## Author

**Tenzin Chonyi** – [LinkedIn](http://www.linkedin.com/in/tenzin-chonyi)
