import os

from telegram import update
from telegram.ext import (Filters, MessageHandler)

def process_sticker_document(bot, update):
    admin = os.getenv('ADMIN')
    if update.message.from_user.username != admin:
        update.message.delete()

sticker_document_handler = MessageHandler(Filters.document | Filters.sticker | Filters.audio | Filters.video | Filters.voice,
                                          process_sticker_document)