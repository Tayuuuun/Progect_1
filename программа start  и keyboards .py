"""
   Обрабатывает команду /start и отправляет приветственное сообщение
   с предложением выбрать действие.
   """

import telebot

API_TOKEN = '8075974197:AAEddxmBUGwPK4IvPo6M0Q-ZfOC9hIA0hEY'
bot = telebot.TeleBot(API_TOKEN)
#ответ бота на старт программы + создаем кнопки
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) #кнопочки
    keyboard.add('новенькое блюдо', 'рецептик') #название кнопочек
    bot.send_message(message.chat.id, 'Здравствуйте, давайте что-нибудь приготовим, запишите рецепт или название блюда', reply_markup=keyboard) #ответ от бота

