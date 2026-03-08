from utils.keyboards import main_menu

def start(bot, message):

    bot.send_message(
        message.chat.id,
        "Welcome to Telegram Coupon Shop",
        reply_markup=main_menu()
    )
