import os

import telebot

from dotenv import load_dotenv

from src.BotHandlers.CallbackHandlers import callback_from_waited_user_handler, callback_func_choose_handler, \
    callback_audio_source_handler
from src.BotHandlers.MessageHandlers import message_from_waited_user_handler, message_start_work_handler, \
    question_message_handler
from src.KeyboardLayouts.InlineKeyboards.AppFuncs import funcs
from src.KeyboardLayouts.InlineKeyboards.AudioSourceKeyboard import audio_sources
from src.classes.UserSourcesInput import user_sources_input

load_dotenv()

token = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(token)


# Common message handler
# In this handler bot defines what type of massage it received and defines its behaviour
@bot.message_handler(func=lambda msg: True)
def messages_handler(message):
    if user_sources_input.is_wait_for_user_input(message.chat.id):
        return message_from_waited_user_handler(bot, message)

    if message.text == "Start work":
        return message_start_work_handler(bot, message)
    else:
        return question_message_handler(bot, message)


# Common callback handler
# In this handler bot defines what type of callback it received and defines its behaviour
@bot.callback_query_handler(func=lambda callback: True)
def callback_handler(callback):
    if user_sources_input.is_wait_for_user_input(callback.message.chat.id):
        return callback_from_waited_user_handler(bot, callback)

    if callback.data in funcs.keys():
        return callback_func_choose_handler(bot, callback)

    if callback.data in audio_sources.keys():
        return callback_audio_source_handler(bot, callback)


bot.infinity_polling()
