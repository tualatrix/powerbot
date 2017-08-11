from telegram.ext import Filters, MessageHandler

def process_new_chat_members(bot, update):
    update.message.delete()

new_members_handler = MessageHandler(Filters.group & Filters.status_update.new_chat_members, process_new_chat_members)