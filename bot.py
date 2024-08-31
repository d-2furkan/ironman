from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                       level=logging.INFO)
logger = logging.getLogger(__name__)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '7479483026:AAHkpkARu7XNJ9H1kZLP_GSGODezrgvqxHs'
YOUR_CHAT_ID = 6155986475

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! Send me a message and I will log your chat ID.')

def log_chat_id(update: Update, context: CallbackContext) -> None:
    """Log the chat ID of any incoming message."""
    chat_id = update.message.chat_id
    if chat_id == YOUR_CHAT_ID:
        logger.info(f'Received message from your chat ID: {chat_id}')
        update.message.reply_text(f'Your chat ID is: {chat_id}')
    else:
        logger.info(f'Received message from another chat ID: {chat_id}')

def main() -> None:
    """Start the bot."""
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # Register command and message handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, log_chat_id))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
