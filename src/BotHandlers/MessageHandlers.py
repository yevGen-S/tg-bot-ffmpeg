import glob
import os
import threading

from telebot import TeleBot

from src.BotHandlers.MediaHandlers import audio_file_handler
from src.KeyboardLayouts.InlineKeyboards.AppFuncs import app_funcs_keyboard
from src.KeyboardLayouts.InlineKeyboards.AudioFuncsKeyboard import audio_speed_func
from src.KeyboardLayouts.InlineKeyboards.AudioSourceKeyboard import audio_source_from_file
from src.KeyboardLayouts.ReplyKeyboards.CommandsKeyboard import starting_keyboard
from src.classes.AudioEditor import AudioEditor
from src.classes.UserInputWaiter import user_input_waiter


# Handler for any message from user from whom the bot is waiting for the source
def message_from_waited_user_handler(bot: TeleBot, message):
    if message.audio and user_input_waiter.is_waiting_for_input(message.chat.id, audio_source_from_file):
        return audio_file_handler(bot, message)

    if user_input_waiter.is_waiting_for_input(message.chat.id, audio_speed_func):
        if -1.0 < float(message.text) <= 5.0:
            user_input_waiter.end_waiting_for_user_input(
                message.chat.id,
                audio_speed_func
            )
            new_message = bot.send_message(
                message.chat.id,
                "Okay! Processing your file..."
            )

            # th = threading.Thread(target=dura, args=(bot, message, new_message))
            # th.start()
            # print("processing file for user: ", message.chat.id)

            file_path = glob.glob(rf".\input_audios\{message.chat.id}.*")[0]
            file_name = file_path[file_path.rindex('\\') + 1:]
            file_format = file_name[file_name.rindex('.') + 1:]
            audio_editor = AudioEditor(file_name)
            audio_editor.change_speed(float(message.text)).save(f"{message.chat.id}", file_format)
            bot.edit_message_text("Done! Have fun!", new_message.chat.id, new_message.id)
            bot.send_audio(message.chat.id, audio=open(rf"./processed/{message.chat.id}.{file_format}", "rb"))
            return

    bot.send_message(
        message.chat.id,
        ', '.join(user_input_waiter.usersInputWaiter.get(message.chat.id))
    )


def dura(bot, message, new_message):
    file_path = glob.glob(rf".\input_audios\{message.chat.id}.*")[0]
    file_name = file_path[file_path.rindex('\\') + 1:]
    file_format = file_name[file_name.rindex('.') + 1:]
    audio_editor = AudioEditor(file_name)
    audio_editor.change_speed(float(message.text)).save(f"{message.chat.id}", file_format)
    bot.edit_message_text("Done! Have fun!", new_message.chat.id, new_message.id)
    bot.send_audio(message.chat.id, audio=open(rf"./processed/{message.chat.id}.{file_format}", "rb"))


# Handler for work starting message "Start work"
def message_start_work_handler(bot, message):
    bot.send_message(
        message.chat.id,
        "Choose function",
        reply_markup=app_funcs_keyboard()
    )


# Handler for
def question_message_handler(bot, message):
    bot.reply_to(
        message,
        "Do you wanna start working?",
        reply_markup=starting_keyboard()
    )
