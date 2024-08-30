from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am your welcome bot. I will greet new members.')

def welcome(update: Update, context: CallbackContext) -> None:
    """Welcome new users to the group."""
    for member in update.message.new_chat_members:
        username = member.username
        if username:
            welcome_message = f"Welcome to the group, @{username}!"
        else:
            welcome_message = "Welcome to the group!"
        update.message.reply_text(welcome_message)

def main() -> None:
    """Start the bot."""
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
