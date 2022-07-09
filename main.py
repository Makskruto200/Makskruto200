import telebot
from telebot import types

bot=telebot.TeleBot("5507373912:AAHkflL8pnvmWEiJLHh8ns8ncircLIPVvEo")

@bot.message_handler(commands=["start"])
def start(message):
     bot.send_message(message.chat.id,"Здраствуй).")
    
bot.polling(none_stop=True)
