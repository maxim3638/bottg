import telebot

token='7727834349:AAG5JC-O9jpKNr6VUENzH35unDvgfwQmHiE'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ ==  '__main__':
     bot.polling()