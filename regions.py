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
        bot.register_next_step_handler(message, characterm)

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
        bot.register_next_step_handler(message, characterl)


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
        bot.register_next_step_handler(message, characterI)

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


def characterm(message):
    if message.text == 'Amber':
        bot.send_message(message.chat.id, 'Рейтинг	D-позиция в тир-листе\n'
                                          'Редкость	⭐️⭐️⭐️⭐️\n'
                                          'Элемент	Пиро🔥')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        amberm = types.KeyboardButton("Main damage dealer")
        ambersup = types.KeyboardButton('Support damage dealer')
        backm = types.KeyboardButton('Back to select characters')
        markup.add(amberm, ambersup)
        markup.add(backm)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterm)
        bot.register_next_step_handler(message, main_damage)


    elif message.text == 'Kaeya':
        bot.send_message(message.chat.id,'Рейтинг	 В-позиция в тир-листе\n'
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
        bot.register_next_step_handler(message, characterm)

    elif message.text == 'Jean':
        bot.send_message(message.chat.id,'Рейтинг	 В-позиция в тир-листе\n'
                                         'Редкость	⭐ ⭐ ⭐ ⭐ ⭐\n'
                                         'Элемент	Анемо🌪️')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        jeansup = types.KeyboardButton("Support damage dealer")
        jheal = types.KeyboardButton("Healer build")
        backm = types.KeyboardButton('Back to select characters')
        markup.add(jeansup, jheal)
        markup.add(backm)
        bot.send_message(message.chat.id, "Выберите нужную вам категорию.", reply_markup=markup)
        bot.register_next_step_handler(message, characterm)

    elif message.text == 'Liza':
        bot.send_message(message.chat.id,'Рейтинг	 C-позиция в тир-листе\n'
                                         'Редкость  ⭐ ⭐ ⭐ ⭐\n'
                                         'Элемент	Электро️⚡️')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        lizam = types.KeyboardButton("Main damage dealer")
        lizasup = types.KeyboardButton("Support damage dealer")
        backm = types.KeyboardButton('Back to select characters')
        markup.add(lizam, lizasup)
        markup.add(backm)
        bot.send_message(message.chat.id, "Выберите нужную вам категорию.", reply_markup=markup)
        bot.register_next_step_handler(message, characterm)

    elif message.text == 'Barbara':
        bot.send_message(message.chat.id,'Рейтинг	 C-позиция в тир-листе\n'
                                         'Редкость  ⭐ ⭐ ⭐ ⭐\n'
                                         'Элемент	Гидро💧')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        lizam = types.KeyboardButton("Bloom damage dealer")
        lizasup = types.KeyboardButton("Support healer build")
        backm = types.KeyboardButton('Back to select characters')
        markup.add(lizam, lizasup)
        markup.add(backm)
        bot.send_message(message.chat.id, "Выберите нужную вам категорию.", reply_markup=markup)
        bot.register_next_step_handler(message, characterm)

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
        bot.register_next_step_handler(message, characterm)

def main_damage(message):
    if message.text == 'Main damage dealer':
        bot.send_message(message.chat.id, 'Для Эмбер в роли мейн-дд подойдут луки на силу атаки или криты, а также те, пассивка которых повышает урон заряженной атаки.\n'
                         'Эмбер нуждается в силе атаки и мастерстве стихий. Данные характеристики можно искать как в часах, так и в дополнительных статах. Корону нужно брать на крит. урон или крит. шанс. Кубок идет на Пиро урон.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        amberarts = types.KeyboardButton('Best artefacts for Amber')
        amberbow = types.KeyboardButton('Best bows for Amber')
        amberback = types.KeyboardButton('Back to choose category')
        markup.add(amberarts, amberbow)
        markup.add(amberback)
        bot.send_message(message.chat.id, 'Выберите оружие или артефакты.', reply_markup=markup)
        bot.register_next_step_handler(message, main_damage)
        bot.register_next_step_handler(message, category)

    elif message.text == 'Support damage dealer':
        bot.send_message(message.chat.id, 'Для Эмбер в качестве саб-дд можно дать оружие, повышающее ее урон с навыков, дающее восстановление энергии, мастерство стихий или полезные усиления для союзников.\n'
                                          'Эмбер нуждается в силе атаки и мастерстве стихий. Данные характеристики можно искать как в часах, так и в дополнительных статах. Корону нужно брать на крит. урон или крит. шанс. Кубок идет на Пиро урон.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        amberartssup = types.KeyboardButton('Best artefacts for Amber in support')
        amberbowsup = types.KeyboardButton('Best bows for Amber in support')
        amberback = types.KeyboardButton('Back to choose category')
        markup.add(amberartssup, amberbowsup)
        markup.add(amberback)
        bot.send_message(message.chat.id, 'Выберите оружие или артефакты.', reply_markup=markup)
        bot.register_next_step_handler(message, main_damage)
        bot.register_next_step_handler(message, categorysup)

    elif message.text == 'Back to choose category':
        bot.send_message(message.chat.id, 'Рейтинг	D-позиция в тир-листе\n'
                                          'Редкость	⭐️⭐️⭐️⭐️\n'
                                          'Элемент	Пиро🔥')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        amberm = types.KeyboardButton("Main damage dealer")
        ambersup = types.KeyboardButton('Support damage dealer')
        backm = types.KeyboardButton('Back to select characters')
        markup.add(amberm, ambersup)
        markup.add(backm)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterm)
        bot.register_next_step_handler(message, main_damage)

def category(message):
    if message.text == 'Best bows for Amber':
        bot.send_message(message.chat.id, 'Top 1\n'
                                          'Первый великий фокус\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          'Базовая атака: 46-608\n'
                                          'Крит. урон:14.4%-66.2%\n'
                                          'Повышает урон заряженной атаки на 16%-32% 🔥. Дарует 1 уровень Уловки за каждого персонажа того же элемента в отряде, что и персонаж с этим луком 🎯. За каждого союзника с другим элементом прибавляет 1 уровень Актерского мастерства 🎭.\n'
                                          'Когда активировано 1/2/3 Уловки, сила атаки возрастает на 16%/32%/48%-32%/64%/96% 💥.\nВ период активации 1/2/3 стаков Актерского мастерства, скорость передвижения увеличивается на 4%/7%/10%-12%/15%/18% 🌟.\n'
                                          'Этот лук идеален для Эмбер, умело играющей от заряженных атак. Обладает великолепной базой, увеличивает критический урон и силу атаки, а также улучшает скорость передвижения 🌪️. Для максимальной эффективности рекомендуется иметь хотя бы одного союзника с элементом Пиро в вашем отряде 🔥.')
        bot.send_message(message.chat.id, 'Top 2\n'
                                          'Лук Амоса\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          'Базовая атака:46-608\n'
                                          'Сила атаки:10.8%-49.6%\n'
                                          'Увеличивает урон обычных и заряженных атак на 12%-24% 💨. Каждые 0.1 секунды полета стрелы увеличивают ее урон на 8%-16% 🔥. Этот эффект может накапливаться до 5 раз.\n'
                                          'Еще одно творение с мощной базой и уникальным уроном через заряженные выстрелы 🏹. Он дарует мощь атаки в изобилии 💥. Особенность лука проявляется в том, что чем дальше находится лучник от цели, тем больше разрушительного урона стрелы приносит 🎯.')
        bot.send_message(message.chat.id, 'Top 3\n'
                                          'Охотничья тропа\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          'Базовая атака:44-542\n'
                                          'Крит. шанс:9.6%-44.1%\n'
                                          'Увеличивает урон всеми элементами на 12%-24% 💥. Каждое попадание заряженной атакой дарует носителю эффект Непрестанной охоты раз в 12 секунд. \n'
                                          'Этот эффект увеличивает урон заряженных атак на 160%-320% от мастерства стихий. Однако через 10 секунд или после 12 активаций эффект исчезает ⏳.\n'
                                          'Лук также повышает критический шанс Эмбер и элементальный урон 🎯. Он идеально подходит героине в отрядах, основанных на реакциях и мастерстве стихий, а также с использованием сета Странствующего ансамбля 🌟.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        backthing = types.KeyboardButton('Back to select wearpon and artefacts')
        markup.add(backthing)
        bot.send_message(message.chat.id, 'Эти луки помогут вам нанести больше урона и облегчить вам игру!', reply_markup=markup)
        bot.register_next_step_handler(message, category)

    elif message.text == 'Best artefacts for Amber':
        bot.send_message(message.chat.id, 'Top 1\n'
                                          'Странствующий ансамбль\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          '2 части: Увеличивает мастерство стихий на 80 единиц 🌀.\n'
                                          '4 части: Увеличивает урон заряженной атаки на 35%, если персонаж использует катализатор или стрелковое оружие 🔥.\n'
                                          'Этот набор идеально подходит для Эмбер, мастера стрелкового искусства 🎯. Он усиливает её мастерство стихий, что способствует более мощным заряженным атакам. \n'
                                          'Комбинированный с использованием катализатора или стрелкового оружия, этот набор артефактов придает её стрелам еще более разрушительную силу 💥.')
        bot.send_message(message.chat.id, 'Top 2\n'
                                          'Горящая алая ведьма\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          '2 части: Увеличивает бонус Пиро урона на 15%.\n'
                                          '4 части: Увеличивает урон реакций Перегрузка, Горение и Цветение на 40%, а урон реакций Пар и Таяние на 15%. \n'
                                          'Использование способности Е-шки увеличивает эффект набора из 2 предметов на 50% на 10 секунд. Этот эффект может накапливаться до 3 раз.\n'
                                          'Этот превосходный набор артефактов идеально подходит для увеличения общего урона Пиро у героини и усиления дамага от закрываемых ею элементальных реакций 🔥.')
        bot.send_message(message.chat.id, 'Top 3\n'
                                          'Воспоминания Симэнавы\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          '2 части: Увеличивает силу атаки на 18%.\n'
                                          '4 части: При использовании способности Е-шки, если у персонажа 15 или более единиц энергии, он теряет 15 единиц энергии. \n'
                                          'Этот набор артефактов отлично подходит для повышения силы атаки и увеличения урона заряженных атак. \n'
                                          'Однако, чтобы воспользоваться его полным потенциалом, придется меньше полагаться на способность Е-шки и более эффективно управлять энергией.В результате урон обычной/заряженной/атаки увеличивается на 50% в течение 10 секунд.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        backthing = types.KeyboardButton('Back to select wearpon and artefacts')
        markup.add(backthing)
        bot.send_message(message.chat.id, 'Эти артефакты помогут вам лучше чувствовать персонажа и облегчить вам игру!', reply_markup=markup)
        bot.register_next_step_handler(message, category)

    elif message.text == 'Back to select wearpon and artefacts':
        bot.send_message(message.chat.id,
                         'Для Эмбер в роли мейн-дд подойдут луки на силу атаки или криты, а также те, пассивка которых повышает урон заряженной атаки.\n'
                         'Эмбер нуждается в силе атаки и мастерстве стихий. Данные характеристики можно искать как в часах, так и в дополнительных статах. Корону нужно брать на крит. урон или крит. шанс. Кубок идет на Пиро урон.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        amberarts = types.KeyboardButton('Best artefacts for Amber')
        amberbow = types.KeyboardButton('Best bows for Amber')
        amberback = types.KeyboardButton('Back to choose category')
        markup.add(amberarts, amberbow)
        markup.add(amberback)
        bot.send_message(message.chat.id, 'Выберите оружие или артефакты.', reply_markup=markup)
        bot.register_next_step_handler(message, main_damage)
        bot.register_next_step_handler(message, category)

def categorysup(message):
    if message.text == 'Best bows for Amber in support':
        bot.send_message(message.chat.id, 'Top 1\n'
                                          'Элегия погибели\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          'Базовая атака:46-608\n'
                                          'Восстановление энергии:12%-55.1%\n'
                                          'Увеличивает мастерство стихий на 60-120 единиц. При попадании способностями Е-шкой или ультой по противнику персонаж получает один Талисман воспоминаний раз в 0.2 секунды, даже когда персонаж в отряде, но не активен.\n'
                                          'Четыре собранных Талисмана воспоминаний пропадают, на 12 секунд наделяя союзников отряда эффектом "Тысячелетняя симфония: Прощальный гимн". Их мастерство стихии повышается на 100-200 единиц, а сила атаки – на 20%-40%. В течение 20 секунд после активации эффекта Талисманы воспоминаний появляться не будут.\n'
                                          'Эффекты Тысячелетней симфонии от оружия того же типа не складываются.\n'
                                          'Это лучшее оружие для Эмбер в роли саб-дд, играющей через реакции. Лук на восстановление энергии позволяет сосредоточиться на более полезных артефактах, повышая эффективность героини. Более того, лук дарует полезные баффы союзникам, усиливая силу всего отряда. 🎶')
        bot.send_message(message.chat.id, 'Top 2\n'
                                          'Небесное крыло\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          'Базовая атака:48-674\n'
                                          'Крит.шанс:4.8%-22.1%\n'
                                          'Повышает критический урон на 20%-40%. При попадании существует 60%-100% шанс нанести 125% физического урона в небольшом радиусе раз в 4-2 секунды.\n'
                                          'Несмотря на отсутствие усилений для союзников, данный лук существенно увеличивает личный урон Эмбер с помощью критических ударов и высокой базы урона. 🔥')
        bot.send_message(message.chat.id, 'Top 3\n'
                                          'Полярная звезда\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          'Базовая атака:46-608\n'
                                          'Крит.шанс:7.2%-33.1%\n'
                                          'Повышает урон от способностей Е-шки и ульты на 12%-24%. Когда любой из навыков попадает по врагу, \n'
                                          'персонаж получает 1 уровень Звезды полярной ночи, который длится 12 секунд. При достижении 1/2/3/4 уровня эффекта, сила атаки повышается на 10/20/30/48%-20/40/60/96%.\n'
                                          'Этот превосходный лук значительно увеличивает урон от элементальных навыков Эмбер и взрыва стихии. Кроме того, он обеспечивает критический шанс и силу атаки. \n'
                                          'Однако это оружие не рекомендуется отдавать Эмбер, если у нее нет четвертого уровня констелляции (С4). 🌌')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        backthingsup = types.KeyboardButton('Back to select wearpon and artefacts')
        markup.add(backthingsup)
        bot.send_message(message.chat.id, 'Эти луки помогут вам сохронять баланс в отряде и облегчить вам игру!', reply_markup=markup)
        bot.register_next_step_handler(message, category)

    elif message.text == 'Best artefacts for Amber in support':
        bot.send_message(message.chat.id, 'Top 1\n'
                                          'Церемония древней знати\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          '2 части: Увеличивает урон взрыва стихии на 20%.\n'
                                          '4 части: Активация ульты увеличивает силу атаки всех членов отряда на 20% в течение 12 секунд. Эффект не складывается.\n'
                                          'Этот универсальный набор артефактов идеален для саппортов. Он усилит взрыв стихий Эмбер и предоставит баффы союзникам. \n'
                                          'Благодаря короткой перезарядке ульты, Эмбер сможет без перерыва поддерживать данное усиление, обеспечивая постоянную поддержку для всего отряда. 🔥🌟\n')
        bot.send_message(message.chat.id, 'Top 2\n'
                                          'Позолоченные сны\n'
                                          '⭐⭐⭐⭐⭐\n'
                                          '2 части: Увеличивает мастерство стихий на 80 единиц.\n'
                                          '4 части: На 8 секунд после вызова реакции, персонаж, носящий этот набор, получает следующие усиления в зависимости от элементов союзников: сила атаки повышается на 14% за каждого персонажа с таким же элементом; мастерство стихий повышается на 50 единиц за каждого персонажа с другим элементом. \n'
                                          'Эффект может возникнуть один раз в 8 секунд. Срабатывает, даже если персонаж с данным набором находится в кармане.\n'
                                          'Этот набор артефактов идеально подходит для Эмбер, играющей в отряде через элементальные реакции. Он повышает статы, а не усиливает способности, поэтому будет действовать на все источники урона в вашем отряде. 🔥🌪️💧⚡')
        bot.send_message(message.chat.id, 'Top 3\n'
                                          'Инструктор\n'
                                          '⭐⭐⭐⭐\n'
                                          '2 части: Увеличивает мастерство стихий на 80 ед.\n'
                                          '4 части: Вызов элементальной реакции увеличивает мастерство стихий всех членов отряда на 120 ед. в течение 8 сек.\n'
                                          'Этот набор артефактов призван повысить мастерство стихий Эмбер и всех членов отряда после вызова элементальной реакции. Он идеально подходит для отрядов, в которых Эмбер выполняет роль поддержки. 💨')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        backthingsup = types.KeyboardButton('Back to select wearpon and artefacts')
        markup.add(backthingsup)
        bot.send_message(message.chat.id, 'Эти артефакты помогут вам сохронять баланс в отряде и облегчить вам игру!',
                         reply_markup=markup)
        bot.register_next_step_handler(message, category)
    elif message.text == 'Back to select wearpon and artefacts':
        bot.send_message(message.chat.id,
                         'Для Эмбер в качестве саб-дд можно дать оружие, повышающее ее урон с навыков, дающее восстановление энергии, мастерство стихий или полезные усиления для союзников.\n'
                         'Эмбер нуждается в силе атаки и мастерстве стихий. Данные характеристики можно искать как в часах, так и в дополнительных статах. Корону нужно брать на крит. урон или крит. шанс. Кубок идет на Пиро урон.')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        amberartssup = types.KeyboardButton('Best artefacts for Amber in support')
        amberbowsup = types.KeyboardButton('Best bows for Amber in support')
        amberback = types.KeyboardButton('Back to choose category')
        markup.add(amberartssup, amberbowsup)
        markup.add(amberback)
        bot.send_message(message.chat.id, 'Выберите оружие или артефакты.', reply_markup=markup)
        bot.register_next_step_handler(message, main_damage)
        bot.register_next_step_handler(message, categorysup)
#-----------------------------------------------------------------------------#
def characterl(message):
    if message.text == 'Shen he':
        bot.send_message(message.chat.id, 'Рейтинг	S-позиция в тир-листе\n'
                                          'Редкость	⭐⭐️️⭐️⭐️⭐️\n'
                                          'Элемент	Крио❄️')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        shenm = types.KeyboardButton("Main damage dealer")
        shensup = types.KeyboardButton('Support damage build')
        backl = types.KeyboardButton('Back to select characters')
        markup.add(shenm, shensup)
        markup.add(backl)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterl)

    elif message.text == 'Zhongli':
        bot.send_message(message.chat.id, 'Рейтинг	S+позиция в тир-листе\n'
                                          'Редкость	⭐⭐️️⭐️⭐️⭐️\n'
                                          'Элемент	Гео🪨')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        zhshild = types.KeyboardButton("Support shield build")
        zhonsup = types.KeyboardButton('Support damage build')
        backl = types.KeyboardButton('Back to select characters')
        markup.add(zhshild, zhonsup)
        markup.add(backl)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterl)

    elif message.text == 'Keqing':
        bot.send_message(message.chat.id, 'Рейтинг	A-позиция в тир-листе\n'
                                          'Редкость	⭐⭐️️⭐️⭐️⭐️\n'
                                          'Элемент	Электро⚡️')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keqm = types.KeyboardButton("Main damage dealer")
        keqagg = types.KeyboardButton('Non-Aggravate damage build')
        backl = types.KeyboardButton('Back to select characters')
        markup.add(keqm, keqagg)
        markup.add(backl)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterl)

    elif message.text == 'Xiao':
        bot.send_message(message.chat.id, 'Рейтинг	А-позиция в тир-листе\n'
                                          'Редкость	⭐⭐️️⭐️⭐️⭐️\n'
                                          'Элемент	Анемо🌪️')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        xiaom = types.KeyboardButton("Main damage dealer")
        xiaom2 = types.KeyboardButton('Alternative main damage build')
        backl = types.KeyboardButton('Back to select characters')
        markup.add(xiaom, xiaom2)
        markup.add(backl)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterl)

    elif message.text == 'Beidou':
        bot.send_message(message.chat.id, 'Рейтинг	А-позиция в тир-листе\n'
                                          'Редкость	⭐⭐️️⭐️️⭐️\n'
                                          'Элемент	Электро⚡️')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        beisup = types.KeyboardButton("Support damage dealer")
        beielec = types.KeyboardButton('Electro damage build')
        backl = types.KeyboardButton('Back to select characters')
        markup.add(beisup, beielec)
        markup.add(backl)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterl)

    elif message.text == 'Back to select characters':
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
        bot.register_next_step_handler(message, characterl)

#----------------------------------------------------------------------#
def characterI(message):
    if message.text == 'Toma':
        bot.send_message(message.chat.id, 'Рейтинг	В-позиция в тир-листе\n'
                                          'Редкость	⭐️️⭐️⭐️⭐️\n'
                                          'Элемент	Пиро🔥')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        tomam = types.KeyboardButton("Support damage dealer")
        tomasup = types.KeyboardButton('Support shield build')
        backi = types.KeyboardButton('Back to select characters')
        markup.add(tomam, tomasup)
        markup.add(backi)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterI)

    elif message.text == 'Kamisato Ayato':
        bot.send_message(message.chat.id, 'Рейтинг	S-позиция в тир-листе\n'
                                          'Редкость	⭐️️⭐️⭐️⭐️⭐️\n'
                                          'Элемент	Гидро💧')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ayatom = types.KeyboardButton("Main damage dealer")
        ayatosup = types.KeyboardButton('Support damage dealer')
        backi = types.KeyboardButton('Back to select characters')
        markup.add(ayatom, ayatosup)
        markup.add(backi)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterI)

    elif message.text == 'Kamisato Ayaka':
        bot.send_message(message.chat.id, 'Рейтинг	S+позиция в тир-листе\n'
                                          'Редкость	⭐️️⭐️⭐️⭐️⭐️\n'
                                          'Элемент	Крио❄️')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ayakam = types.KeyboardButton("Main damage dealer")
        backi = types.KeyboardButton('Back to select characters')
        markup.add(ayakam)
        markup.add(backi)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterI)

    elif message.text == 'Arataki Itto':
        bot.send_message(message.chat.id, 'Рейтинг	S-позиция в тир-листе\n'
                                          'Редкость	⭐️️⭐️⭐️⭐️⭐️\n'
                                          'Элемент  Гео🪨')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ittom = types.KeyboardButton("Main damage dealer")
        backi = types.KeyboardButton('Back to select characters')
        markup.add(ittom)
        markup.add(backi)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterI)

    elif message.text == 'Raiden Shogun':
        bot.send_message(message.chat.id, 'Рейтинг	S+позиция в тир-листе\n'
                                          'Редкость	⭐️️⭐️⭐️⭐️⭐️\n'
                                          'Элемент  Электро⚡️')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        shogm = types.KeyboardButton("Main damage dealer")
        shogsup = types.KeyboardButton("Hyperbloom support build")
        backi = types.KeyboardButton('Back to select characters')
        markup.add(shogm, shogsup)
        markup.add(backi)
        bot.send_message(message.chat.id, 'Выберите нужную вам категорию.', reply_markup=markup)
        bot.register_next_step_handler(message, characterI)

    elif message.text == 'Back to select characters':
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
        bot.register_next_step_handler(message, characterI)


bot.polling(none_stop=True)
