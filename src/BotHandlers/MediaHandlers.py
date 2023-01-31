from telebot import TeleBot

from src.KeyboardLayouts.InlineKeyboards.AudioSourceKeyboard import audio_source_from_file
from src.classes.UserInputWaiter import user_input_waiter
from src.classes.YouTubeLoader import YouTubeLoader, user_youtube_downloaders
from src.utils.UserFilesLoader import user_files_downloaders, UserFilesDownloader


# Handler for audio file message
def audio_file_handler(bot: TeleBot, message):
    index_before_format = 0
    try:
        index_before_format = message.audio.file_name.rindex('.')
    except ValueError:
        bot.send_message(message.chat.id, "Sorry, I can't recognize file format, try another file with correct format")
        return

    new_message = bot.send_message(message.chat.id, "Got it! Downloading your file...")
    downloader = UserFilesDownloader(bot, message.chat.id, new_message.id)
    user_files_downloaders[message.chat.id] = downloader
    downloader.download_user_audio_file(
        bot.get_file(message.audio.file_id).file_path,
        message.audio.file_name[index_before_format + 1:]
    )


# Handler for YouTube link message
def youtube_link_audio_handler(bot: TeleBot, message):
    if (r"youtube.com" not in message.text) and (r"youtu.be" not in message.text):
        return bot.send_message(
            message.chat.id,
            "This is not valid YouTube link"
        )

    new_message = bot.send_message(message.chat.id, "Got it! Downloading your file...")
    downloader = YouTubeLoader(bot, message.chat.id, new_message.message_id, 'audio', message.text)
    user_youtube_downloaders[message.chat.id] = downloader
    downloader.load_user_file()


# Handler for audio file message
def video_file_handler(bot: TeleBot, message):
    index_before_format = 0
    try:
        index_before_format = message.video.file_name.rindex('.')
    except ValueError:
        bot.send_message(message.chat.id, "Sorry, I can't recognize file format, try another file with correct format")
        return

    new_message = bot.send_message(message.chat.id, "Got it! Downloading your file...")
    downloader = UserFilesDownloader(bot, message.chat.id, new_message.id)
    user_files_downloaders[message.chat.id] = downloader
    downloader.download_user_video_file(
        bot.get_file(message.video.file_id).file_path,
        message.video.file_name[index_before_format + 1:]
    )
