import telebot
from telebot.types import Message
import csv

from urllib3.filepost import writer

TOKEN = '7151573905:AAG2VvqD8fPIe0SWvTr7Yfs_IqcK_1eW-lw'
bot = telebot.TeleBot(TOKEN)

new_list = []


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message, "Привет! Я бот для управления чатом. Напиши /help, чтобы узнать, что я умею.")


@bot.message_handler(commands=['help'])
def help(message: Message):
    bot.reply_to(message, '/show to show the history of the chat')


# @bot.message_handler(func=lambda message: True)
# def save_message(message: Message):
#     if not message.text.startswith('/'):
#         new_list.append(message.text)
#         bot.reply_to(message, f'here you have a list with your messagesin russia inside the chat: {new_list}')

@bot.message_handler(commands=['show'])
def show(message: Message):
    chat_id = message.chat.id
    with open('members.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        messages = [''.join(row) for row in reader]

    bot.send_message(chat_id, "\n".join(messages) if messages else "No messages saved.")


@bot.message_handler(func=lambda message: True)
def storing(message: Message):
    with open('members.csv', 'a', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow([message.chat.id, message.from_user.id, message.text])
        bot.send_message(message.chat.id, "your message was stored in csv file")
    print(f"Message saved: {message.text}")


bot.polling()
