from src.KeyboardLayouts.InlineKeyboards.AppFuncs import app_func_audio_work, app_func_video_work
from src.KeyboardLayouts.InlineKeyboards.AudioFuncsKeyboard import audio_speed_func
from src.KeyboardLayouts.InlineKeyboards.AudioSourceKeyboard import audio_sources_keyboard, audio_sources
from src.KeyboardLayouts.InlineKeyboards.VideoSourceKeyboard import video_sources_keyboard, video_sources
from src.classes.UserInputWaiter import user_input_waiter


def callback_from_waited_user_handler(bot, callback):
    bot.send_message(
        callback.message.chat.id,
        ', '.join(user_input_waiter.usersInputWaiter.get(callback.message.chat.id))
    )


# Handler for app function selection via inline keyboard
def callback_func_choose_handler(bot, callback):
    new_message = ''
    new_keyboard = ''

    if callback.data == app_func_audio_work:
        new_message = 'Choose audio source'
        new_keyboard = audio_sources_keyboard()

    if callback.data == app_func_video_work:
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
    user_input_waiter.add_user_input_waiter(callback.message.chat.id, callback.data)

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
    user_input_waiter.add_user_input_waiter(callback.message.chat.id, callback.data)

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


# Handler for audio function selection via inline keyboard
def callback_audio_func_handler(bot, callback):
    # Delete Keyboard
    bot.edit_message_reply_markup(callback.message.chat.id,
                                  callback.message.message_id,
                                  reply_markup=None)

    if callback.data == audio_speed_func:
        user_input_waiter.add_user_input_waiter(callback.message.chat.id, callback.data)
        return bot.edit_message_text(
                   'Enter speed ratio. It must be from 0 to 3 (excludes 0). %0A' +
                   'Passing 1 does not change audio speed. %0A' +
                   '(format: [digits].[digits])',
                   callback.message.chat.id,
                   callback.message.message_id
               )

    # Edit message for chosen function
    bot.edit_message_text(
        'You have chosen ' + audio_sources[callback.data],
        callback.message.chat.id,
        callback.message.message_id
    )