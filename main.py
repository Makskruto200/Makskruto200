import telebot
from telebot import types
import random
bot=telebot.TeleBot("5507373912:AAHkflL8pnvmWEiJLHh8ns8ncircLIPVvEo")

#приветствие
@bot.message_handler(commands=["start"])
def start(message):
     bot.send_message(message.chat.id,"Добро пожаловать!.")


#рандомная загадка 
@bot.message_handler(commands=["rs"])
def random_secret(message):
     secret_list=["Сколько ножек у осминожка?","777"]
     bot.send_message(message.chat.id,random.randint(0,9))

    

bot.polling(none_stop=True)
