import telebot
from config import BOT_TOKEN
from handlers.start import start

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])

def start_command(message):

    start(bot, message)

bot.infinity_polling()
