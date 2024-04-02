import telebot
from telebot import types

bot = telebot.TeleBot('6454801259:AAFbfIaOhhS2RMV3uYSr5SVCjMRio73N0ts')

def on_click(message):
    if message.text == 'Mondstadt':
        markup = types.ReplyKeyboardMarkup()
        amber = types.KeyboardButton('Amber')
        markup.row(amber)
        bot.send_message(message.chat.id, 'Выберите персонажа', reply_markup=markup)

bot.polling(none_stop=True)
