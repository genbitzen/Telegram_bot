from turtle import update
import Constants as keys
from telegram.ext import * 
import Responses as R
import logging

print("Bot started...")

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    chat_id = get_chat_id(update,context)
    user = get_user(update,context)
    update.message.reply_text(f"Type something random to get started {user}!")
    
    
def help(update, context):
    update.message.reply_text('Ask google?')

def get_user(update, context):
    return update.message.chat.username

def get_chat_id(update, context):
    chat_id = -1
    if update.message is not None:
        chat_id = update.message.chat_id
    elif update.callback_query is not None:
        chat_id = update.callback_query.message.chat_id
    elif update.poll is not None:
        chat_id = context.bot_data[update.poll.id]
    return chat_id

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def echo(update, context):
    update.message.reply_text(update.message.text)

def error(update, context):
    logger.warning(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text,handle_message))
    
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()