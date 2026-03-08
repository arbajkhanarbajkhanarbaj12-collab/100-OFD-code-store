from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():

    markup = InlineKeyboardMarkup()

    markup.add(
        InlineKeyboardButton("🛒 Shop", callback_data="shop")
    )

    markup.add(
        InlineKeyboardButton("🎁 Redeem Gift", callback_data="redeem")
    )

    markup.add(
        InlineKeyboardButton("💰 Wallet", callback_data="wallet")
    )

    return markup
