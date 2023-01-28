import os
import urllib.request

from dotenv import load_dotenv
from telebot import TeleBot

from src.KeyboardLayouts.InlineKeyboards.AudioFuncsKeyboard import audio_funcs_keyboard

load_dotenv()

token = os.environ.get("BOT_TOKEN")

"""
    Class for downloading/uploading user files
"""


class UserFilesDownloader:
    def __init__(self, bot, user_id, message_id):
        self.bot = bot
        self.current_user_id = user_id
        self.current_message_id = message_id

    # Download audio file
    def download_user_audio_file(self, file_path, file_format):
        urllib.request.urlretrieve(
            rf'https://api.telegram.org/file/bot{token}/{file_path}',
            rf'input_audios\{self.current_user_id}.{file_format}',
            reporthook=self.user_file_downloader_callback
        )

    # Download user file
    def download_user_file(self, file_path, file_format):
        urllib.request.urlretrieve(
            rf'https://api.telegram.org/file/bot{token}/{file_path}',
            rf'tmp{self.current_user_id}.{file_format}'
        )

    # User file downloader callback
    # It passed to urlretrieve
    def user_file_downloader_callback(self, current_blocks, block_size, file_size):
        if current_blocks * block_size >= file_size:
            self.bot.edit_message_text(
                "File downloaded. Choose function you want to execute",
                self.current_user_id,
                self.current_message_id,
                reply_markup=audio_funcs_keyboard()
            )
            user_files_downloaders.__delitem__(self.current_user_id)


# Dictionary for downloaders
# "user_id": "downloader"
user_files_downloaders = {}
