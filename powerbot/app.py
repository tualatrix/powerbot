import os

from telegram.ext import (Updater, CommandHandler)

from handlers.new_members_handler import new_members_handler
from handlers.start_handler import start_handler
from handlers.sticker_document_handler import sticker_document_handler

def error_handler(bot, update, error):
    print('Update "%s" caused error "%s"' % (update, error))

def run():
    token = os.getenv('TELEGRAM_TOKEN')

    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(new_members_handler)
    dispatcher.add_handler(sticker_document_handler)
    dispatcher.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    run()