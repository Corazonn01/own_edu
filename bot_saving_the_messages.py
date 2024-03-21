import telebot
from telebot.types import Message

TOKEN = '7151573905:AAG2VvqD8fPIe0SWvTr7Yfs_IqcK_1eW-lw'
bot = telebot.TeleBot(TOKEN)

new_list = []


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message,
                 f'Привет! Пожалуйста, напишите что-нибудь. Каждое ваше сообщение будет сохранено в моей системе.')


# @bot.message_handler(func=lambda message: True)
# def save_message(message: Message):
#     new_list.append(message.text)
#     bot.reply_to(message, f'here you have a list with your messages inside the chat: {new_list}')


@bot.message_handler(func=lambda message: True)
def storing(message: Message):
    with open('members.csv', 'a', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow([message.chat.id, message.from_user.id, message.text])
        bot.send_message(message.chat.id, "your message was stored in csv file")
    print(f"Message saved: {message.text}")


@bot.message_handler(func=lambda message: True)
def show(message: Message):
    chat_id = message.chat.id
    with open('members.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        messages = [''.join(row) for row in reader]

    bot.send_message(chat_id, "\n".join(messages) if messages else "No messages saved.")

bot.polling()





