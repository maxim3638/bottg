import telebot #Імпортується бібліотека telebot

token='7727834349:AAG5JC-O9jpKNr6VUENzH35unDvgfwQmHiE' #унікальний ключ доступу Telegram-бота. Токен видається через BotFather у Telegram під час створення нового бота.

bot = telebot.TeleBot(token) #створення екземпляра бота.

@bot.message_handler(content_types=["text"]) #Декоратор, який визначає обробник для певних типів повідомлень.
def repeat_all_messages(message): #Це функція, яка буде викликатися, коли бот отримує текстове повідомлення.
    bot.send_message(message.chat.id, message.text) #Надсилається відповідь користувачу.повторює повідомлення

if __name__ ==  '__main__': #перевіряє, чи файл запускається напряму, а не імпортується як модуль в інший файл.Якщо файл запускається, виконується код нижче
     bot.polling() #запускає безперервний процес опитування серверів Telegram
