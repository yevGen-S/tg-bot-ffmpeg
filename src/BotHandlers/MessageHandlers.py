from src.KeyboardLayouts.InlineKeyboards.AppFuncs import app_funcs_keyboard
from src.KeyboardLayouts.ReplyKeyboards.CommandsKeyboard import starting_keyboard
from src.classes.UserSourcesInput import user_sources_input


# Handler for any message from user from whom the bot is waiting for the source
def message_from_waited_user_handler(bot, message):
    bot.send_message(
        message.chat.id,
        ', '.join(user_sources_input.usersInputWaiter.get(message.chat.id))
    )


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
