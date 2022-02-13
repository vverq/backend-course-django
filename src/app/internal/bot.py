import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from transport.bot import handlers

API_KEY = os.environ['API_KEY']


class Bot:
    def __init__(self, api_key):
        self.api_key = api_key
        self.updater = Updater(api_key)
        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(CommandHandler("start", handlers.start))
        self.dispatcher.add_handler(CommandHandler("set_phone", handlers.share_phone))
        self.dispatcher.add_handler(CommandHandler("me", handlers.me))
        self.dispatcher.add_handler(MessageHandler(Filters.contact, handlers.update_phone))


def main():
    bot = Bot(API_KEY)
    bot.updater.start_polling()
    bot.updater.idle()


if __name__ == '__main__':
    main()

