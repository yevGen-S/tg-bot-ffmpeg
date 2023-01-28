from telebot import TeleBot

from src.KeyboardLayouts.InlineKeyboards.AudioSourceKeyboard import audio_source_from_file
from src.classes.UserInputWaiter import user_input_waiter
from src.utils.UserFilesLoader import user_files_downloaders, UserFilesDownloader


# Handler for audio file message
def audio_file_handler(bot: TeleBot, message):
    index_before_format = 0
    try:
        index_before_format = message.audio.file_name.rindex('.')
    except ValueError:
        bot.send_message(message.chat.id, "Sorry, I can't recognize file format, try another file with correct format")
        user_input_waiter.end_waiting_for_user_input(message.chat.id, audio_source_from_file)

    new_message = bot.send_message(message.chat.id, "Got it! Downloading your file...")
    downloader = UserFilesDownloader(bot, message.chat.id, new_message.id)
    user_files_downloaders[message.chat.id] = downloader
    downloader.download_user_audio_file(
        bot.get_file(message.audio.file_id).file_path,
        message.audio.file_name[index_before_format + 1:]
    )
    print("downloaded for: ", message.chat.id)
