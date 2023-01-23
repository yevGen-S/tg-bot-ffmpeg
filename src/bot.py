import os

import telebot

from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "How are you doing?")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
