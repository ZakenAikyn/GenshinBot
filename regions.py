import time

import telebot
from telebot import types

bot = telebot.TeleBot('6454801259:AAFbfIaOhhS2RMV3uYSr5SVCjMRio73N0ts')


@bot.message_handler(commands=['start'])
def regions(message):
    markup = types.ReplyKeyboardMarkup()
    mond = types.KeyboardButton('Mondstadt')
    lyuie = types.KeyboardButton('Lyuie')
    inaz = types.KeyboardButton('Inazuma')
    sum = types.KeyboardButton('Sumery')
    font = types.KeyboardButton('Fontaine')
    markup.row(mond, lyuie)
    markup.row(inaz, sum)
    markup.row(font)
    bot.send_message(message.chat.id, 'Приветствую дорогой путешественник!\n'
                                      'Выберите регион который вам нужен.', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Mondstadt':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        amber = types.KeyboardButton('Amber')
        kaeya = types.KeyboardButton('Kaeya')
        jean = types.KeyboardButton('Jean')
        liza = types.KeyboardButton('Liza')
        barb = types.KeyboardButton('Barbara')
        backr = types.KeyboardButton('Back to regions')
        markup.add(amber, kaeya, jean, liza, barb)
        markup.row(backr)
        bot.send_message(message.chat.id, 'Выберите персонажа', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)
        bot.register_next_step_handler(message, character)

    elif message.text == 'Lyuie':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        shen_he = types.KeyboardButton('Shen he')
        zhongli = types.KeyboardButton('Zhongli')
        keqing = types.KeyboardButton('Keqing')
        xiao = types.KeyboardButton('Xiao')
        beidou = types.KeyboardButton('Beidou')
        backr = types.KeyboardButton('Back to regions')
        markup.add(shen_he, zhongli, keqing, xiao, beidou)
        markup.row(backr)
        bot.send_message(message.chat.id, 'Выберите персонажа', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)

    elif message.text == 'Inazuma':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        toma = types.KeyboardButton('Toma')
        ayato = types.KeyboardButton('Kamisato Ayato')
        ayaka = types.KeyboardButton('Kamisato Ayaka')
        itto = types.KeyboardButton('Arataki Itto')
        raiden = types.KeyboardButton('Raiden Shogun')
        backr = types.KeyboardButton('Back to regions')
        markup.add(toma, ayato, ayaka, itto, raiden)
        markup.row(backr)
        bot.send_message(message.chat.id, 'Выберите персонажа', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)

    elif message.text == 'Sumery':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        nahida = types.KeyboardButton('Nahida')
        tignari = types.KeyboardButton('Tignari')
        cyno = types.KeyboardButton('Cyno')
        collei = types.KeyboardButton('Collei')
        dori = types.KeyboardButton('Dori')
        backr = types.KeyboardButton('Back to regions')
        markup.add(nahida, tignari, cyno, collei, dori)
        markup.row(backr)
        bot.send_message(message.chat.id, 'Выберите персонажа', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)

    elif message.text == 'Fontaine':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        navia = types.KeyboardButton('Navia')
        furina = types.KeyboardButton('Furina')
        lyney = types.KeyboardButton('Lyney')
        freminet = types.KeyboardButton('Freminet')
        neuvillete = types.KeyboardButton('Neuvillete')
        backr = types.KeyboardButton('Back to regions')
        markup.add(navia, furina, freminet, neuvillete, lyney)
        markup.row(backr)
        bot.send_message(message.chat.id, 'Выберите персонажа', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)

    elif message.text == 'Back to regions':
        markup = types.ReplyKeyboardMarkup()
        mond = types.KeyboardButton('Mondstadt')
        lyuie = types.KeyboardButton('Lyuie')
        inaz = types.KeyboardButton('Inazuma')
        sum = types.KeyboardButton('Sumery')
        font = types.KeyboardButton('Fontaine')
        markup.row(mond, lyuie)
        markup.row(inaz, sum)
        markup.row(font)
        bot.send_message(message.chat.id, 'Выберите регион который вам нужен.', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)


def character(message):
    if message.text == 'Amber':
        bot.send_message(message.chat.id, 'Рейтинг	D-позиция в тир-листе\n'
                                          'Редкость	⭐️⭐️⭐️⭐️\n'
                                          'Элемент	Пиро🔥')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        amberm = types.KeyboardButton("Main_damage_dealer")
        ambersup = types.KeyboardButton('Support damage dealer')
        backm = types.KeyboardButton('Back to select characters')
        markup.add(amberm, ambersup)
        markup.add(backm)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, character)

    elif message.text == 'Kaeya':
        bot.send_message(message.chat.id, 'Рейтинг	 В-позиция в тир-листе\n'
                         'Редкость	⭐ ⭐ ⭐ ⭐\n'
                         'Элемент	Крио❄️')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keayam = types.KeyboardButton("Main damage dealer")
        keayasup = types.KeyboardButton("Support damage dealer")
        kcryo = types.KeyboardButton("Cryo damage build")
        kphyc = types.KeyboardButton("Physical damage build")
        backm = types.KeyboardButton('Back to select characters')
        markup.add(keayam, keayasup, kcryo, kphyc)
        markup.add(backm)
        bot.send_message(message.chat.id, "Выберите нужную вам категорию.", reply_markup=markup)
        bot.register_next_step_handler(message, character)

    elif message.text == 'Back to select characters':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        amber = types.KeyboardButton('Amber')
        kaeya = types.KeyboardButton('Kaeya')
        jean = types.KeyboardButton('Jean')
        liza = types.KeyboardButton('Liza')
        barb = types.KeyboardButton('Barbara')
        backr = types.KeyboardButton('Back to regions')
        markup.add(amber, kaeya, jean, liza, barb)
        markup.row(backr)
        bot.send_message(message.chat.id, 'Выберите персонажа', reply_markup=markup)
        bot.register_next_step_handler(message, on_click)
        bot.register_next_step_handler(message, character)

bot.polling(none_stop=True)
