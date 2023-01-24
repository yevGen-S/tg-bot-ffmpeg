from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

funcs_in_row = 1

'''
    Functions dictionary: "callback data": "function name in tg"
'''
func_audio_work = 'audio_work'
func_video_work = 'video_work'
funcs = {
    func_audio_work: 'Work with audio',
    func_video_work: 'Work with video'
}


# Get inline keyboard for app functions
def app_funcs_keyboard():
    markup = InlineKeyboardMarkup()
    markup.row_width = funcs_in_row

    for key, value in funcs.items():
        markup.add(InlineKeyboardButton(value, callback_data=key))

    return markup
