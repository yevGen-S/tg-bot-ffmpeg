from src.KeyboardLayouts.InlineKeyboards.AppFuncs import func_audio_work, func_video_work
from src.KeyboardLayouts.InlineKeyboards.AudioSourceKeyboard import audio_sources_keyboard, audio_sources
from src.KeyboardLayouts.InlineKeyboards.VideoSourceKeyboard import video_sources_keyboard, video_sources
from src.classes.UserSourcesInput import user_sources_input


def callback_from_waited_user_handler(bot, callback):
    bot.send_message(
        callback.message.chat.id,
        ', '.join(user_sources_input.usersInputWaiter.get(callback.message.chat.id))
    )


# Handler for app function selection via inline keyboard
def callback_func_choose_handler(bot, callback):
    new_message = ''
    new_keyboard = ''

    if callback.data == func_audio_work:
        new_message = 'Choose audio source'
        new_keyboard = audio_sources_keyboard()

    if callback.data == func_video_work:
        new_message = 'Choose video source'
        new_keyboard = video_sources_keyboard()

    # Edit message for chosen function
    bot.edit_message_text(
        new_message,
        callback.message.chat.id,
        callback.message.message_id,
        reply_markup=new_keyboard
    )


# Handler for audio source selection via inline keyboard
def callback_audio_source_handler(bot, callback):
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


# Handler for video source selection via inline keyboard
def callback_video_source_handler(bot, callback):
    user_sources_input.add_user_input_waiter(callback.message.chat.id, callback.data)

    # Delete Keyboard
    bot.edit_message_reply_markup(callback.message.chat.id,
                                  callback.message.message_id,
                                  reply_markup=None)

    # Edit message for chosen function
    bot.edit_message_text(
        'You have chosen ' + video_sources[callback.data],
        callback.message.chat.id,
        callback.message.message_id
    )
