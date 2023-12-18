# Telegram Bot for Monitoring URL Status

This bot sends the request status of the specified URL to Telegram chats and notifies about problems.

## Installation and Launch

1. Install the necessary libraries:

     ```bash
     pip install requests python-telegram-bot
     ```

2. Replace the values of the `URL` and `TOKEN` variables in the code with your actual values:

     ```python
     URL = 'YOUR_URL'
     TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
     ```

3. Run the script:

     ```bash
     python main.py
     ```

## Usage

1. The bot regularly sends a request to the specified URL and checks the status of the response.
2. If the status is not 404, the bot sends the status to Telegram chats.
3. In case of an error (exception), the bot sends an error notification.
