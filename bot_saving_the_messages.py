import telebot
from telebot.types import Message

TOKEN = '7151573905:AAG2VvqD8fPIe0SWvTr7Yfs_IqcK_1eW-lw'
bot = telebot.TeleBot(TOKEN)

# new_list = []


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message,
                 f'Привет! Пожалуйста, напишите что-нибудь. Каждое ваше сообщение будет сохранено в моей системе.')
    # user_answer = message.text
    # new_list.append(user_answer)


@bot.message_handler(commands=['stats'])
def stats(message: Message):
    chat_id = message.chat.id
    if chat_id not in stats:
        return "Статистика чата пуста"
    else:
        total_messages = stats[chat_id]['total_messages']
        unique_users = len(stats[chat_id]['users'])
        bot.reply_to(message,
                     f"Статистика чата:\nВсего сообщений: {total_messages}\nУникальных пользователей: {unique_users}")


# bot.polling()
try:
    bot.polling()
except Exception as e:
    print(e)
