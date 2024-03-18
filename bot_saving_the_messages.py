import telebot
from telebot.types import Message

TOKEN = '7151573905:AAG2VvqD8fPIe0SWvTr7Yfs_IqcK_1eW-lw'
bot = telebot.TeleBot(TOKEN)

new_list = []


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message,
                 f'Привет! Пожалуйста, напишите что-нибудь. Каждое ваше сообщение будет сохранено в моей системе.')


@bot.message_handler(func=lambda message: True)
def save_message(message: Message):
    new_list.append(message.text)
    bot.reply_to(message, f'here you have a list with your messages inside the chat: {new_list}')


bot.polling()
