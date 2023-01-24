from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

sources_in_row = 1

"""
    Audio sources dictionary: "callback data": "video_source"
"""
from_video_file = 'from_video_file'
from_youtube_video = 'from_youtube_video'
video_sources = {
    from_video_file: 'Load as video file',
    from_youtube_video: 'Load as youtube link'
}


# Get inline keyboard for audio sources
def video_sources_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = sources_in_row

    for key, value in video_sources.items():
        markup.add(InlineKeyboardButton(value, callback_data=key))

    return markup
