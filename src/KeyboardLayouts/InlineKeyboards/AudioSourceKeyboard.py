from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

sources_in_row = 1

"""
    Audio sources dictionary: "callback data": "audio_source"
"""
from_audio_file = 'from_audio_file'
from_youtube_audio = 'from_youtube_audio'
audio_sources = {
    from_audio_file: 'Load as audio file',
    from_youtube_audio: 'Load as youtube link'
}


# Get inline keyboard for audio sources
def audio_sources_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = sources_in_row

    for key, value in audio_sources.items():
        markup.add(InlineKeyboardButton(value, callback_data=key))

    return markup
