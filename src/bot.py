import os

import telebot

from dotenv import load_dotenv

from src.KeyboardLayouts.InlineKeyboards.AppFuncs import app_funcs_keyboard, funcs, func_audio_work
from src.KeyboardLayouts.InlineKeyboards.AudioSourceKeyboard import audio_sources_keyboard, audio_sources
from src.KeyboardLayouts.ReplyKeyboards.CommandsKeyboard import starting_keyboard
from src.classes.UserSourcesInput import user_sources_input

load_dotenv()

token = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(token)


# Edit message on function selection callback
@bot.callback_query_handler(func=lambda callback: callback.data in funcs.keys() and
                                                  not user_sources_input.is_wait_for_user_input(
                                                      callback.message.chat.id
                                                  ))
def choose_func(callback):
    new_message = ''
    new_keyboard = ''

    if callback.data == func_audio_work:
        new_message = 'Choose audio source'
        new_keyboard = audio_sources_keyboard()

    # Edit message for chosen function
    bot.edit_message_text(
        new_message,
        callback.message.chat.id,
        callback.message.message_id,
        reply_markup=new_keyboard
    )


# Edit message on audio source selection callback
@bot.callback_query_handler(func=lambda callback: callback.data in audio_sources.keys() and
                                                  not user_sources_input.is_wait_for_user_input(
                                                      callback.message.chat.id
                                                  ))
def choose_func(callback):
    user_sources_input.add_user_input_waiter(callback.message.chat.id, callback.data)

    # Delete Keyboard
    bot.edit_message_reply_markup(callback.message.chat.id,
                                  callback.message.message_id,
                                  reply_markup=None)

    # Edit message for chosen function
    bot.edit_message_text(
        'You have chosen ' + audio_sources[callback.data],
        callback.message.chat.id,
        callback.message.message_id
    )


# Answer on "Start work" message
@bot.message_handler(func=lambda msg: str(msg.text) == "Start work" and
                                      not user_sources_input.is_wait_for_user_input(msg.chat.id))
def start_work(message):
    bot.send_message(message.chat.id, "Choose function", reply_markup=app_funcs_keyboard())


# Default answer for other messages
@bot.message_handler(func=lambda msg: str(msg.text) != "Start work")
def echo_all(message):
    if user_sources_input.is_wait_for_user_input(message.chat.id):
        bot.send_message(
            message.chat.id,
            ', '.join(user_sources_input.usersInputWaiter.get(message.chat.id))
        )
        return

    bot.reply_to(message, "Do you wanna start working?", reply_markup=starting_keyboard())


bot.infinity_polling()
