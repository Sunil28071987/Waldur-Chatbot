#!/usr/bin/env python
# coding: utf-8

from telegram.ext import Updater, MessageHandler, Filters
import requests as r

backend_url = "http://localhost:4567/"


def query(bot, update):
    response = r.request("GET", backend_url + update.message.text)
    update.message.reply_text(response.text)


def main():
    updater = Updater(read_token())

    dp = updater.dispatcher

    # responds to any message that starts with '/'
    dp.add_handler(MessageHandler(Filters.command, query))

    updater.start_polling()

    updater.idle()


def read_token():
    with open('.token', 'r') as token:
        return token.read()


if __name__ == '__main__':
    main()