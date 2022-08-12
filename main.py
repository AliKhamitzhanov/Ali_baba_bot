from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, audio
from aiogram.utils import executor
from config import bot, dp
import logging
import random


@dp.message_handler(commands=['start'])
async def mem(message: types.Message):
    await bot.send_message(message.chat.id, f"СИСТЕМА ГАЧИМУЧИ ОТКРЫЛАСЬ!\n"
                                            f"Еели хотиет стать кем то пройдите тест -> /quiz\n"
                                            f"Если хотите увидеть рандомный мем -> /mem\n"
                                            f"Если вым нужны видео со смыслом то вам ко мне -> /video\n"
                                            f"Если вам не хватает мотивации то вам суда -> /motivationVideo",)

#mem
@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photos = ["imges/image1.jpg", "imges/image2.jpg", "imges/image3.jpg", "imges/image4.jpg", "imges/image5.jpg",\
              "imges/image6.jpg", "imges/image7.jpg", "imges/image8.jpg", "imges/image9.jpg","imges/image10.jpg",]

    imges = open(random.choice(photos), 'rb')

    await bot.send_photo(message.chat.id, photo=imges)

#music
@dp.message_handler(commands=['music'])
async def music(message: types.Message):
    music = [
        "music/Harry_Styles_-_Watermelon_Sugar_67429150.mp3",
        "music/instasamka-moja-kiska-dlja-nego-vsegda-gotova_(kztrack.kz).mp3",
        "music/Lil_Nas_X_Jack_Harlow_-_INDUSTRY_BABY_73061759.mp3",
        "music/Lizzo_-_About_Damn_Time_74115343.mp3",
        "music/Melanie_Martinez_-_Cake_48195644.mp3",

        "music/Naruto Shippuden OST — Opening №1 (www.lightaudio.ru).mp3",
        "music/opening_1_sezona_-_Klinok_rassekayushhijj_demonov_65423151.mp3",
        "music/OST_Naruto_shippuden_Ikimono-gakari_-_Blue_Bird_OP3_62967143.mp3",
        "music/Vance_Joy_-_Missing_Piece_73152511.mp3",
        "music/Vance_Joy_-_Riptide_47960565.mp3",
    ]

    audio = open(random.choice(music), 'rb')
    await message.reply(f"Подождите идет загруска музыки!")
    await bot.send_audio(message.chat.id, audio=audio)

#allmusic
@dp.message_handler(commands=['allmusic'])
async def music(message: types.Message):


    audio1 = open("music/Harry_Styles_-_Watermelon_Sugar_67429150.mp3", 'rb')
    audio2 = open("music/instasamka-moja-kiska-dlja-nego-vsegda-gotova_(kztrack.kz).mp3", 'rb')
    audio3 = open("music/Lil_Nas_X_Jack_Harlow_-_INDUSTRY_BABY_73061759.mp3", 'rb')
    audio4 = open("music/Lizzo_-_About_Damn_Time_74115343.mp3", 'rb')
    audio5 = open("music/Melanie_Martinez_-_Cake_48195644.mp3", 'rb')
    audio6 = open("music/Naruto Shippuden OST — Opening №1 (www.lightaudio.ru).mp3", 'rb')
    audio7 = open("music/opening_1_sezona_-_Klinok_rassekayushhijj_demonov_65423151.mp3", 'rb')
    audio8 = open("music/OST_Naruto_shippuden_Ikimono-gakari_-_Blue_Bird_OP3_62967143.mp3", 'rb')
    audio9 = open("music/Vance_Joy_-_Missing_Piece_73152511.mp3", 'rb')
    audio10 = open("music/Vance_Joy_-_Riptide_47960565.mp3", 'rb')

    await message.reply(f"Подождите идет загруска всей музыки!")
    await bot.send_audio(message.chat.id, audio=audio1)
    await bot.send_audio(message.chat.id, audio=audio2)
    await bot.send_audio(message.chat.id, audio=audio3)
    await bot.send_audio(message.chat.id, audio=audio4)
    await bot.send_audio(message.chat.id, audio=audio5)
    await bot.send_audio(message.chat.id, audio=audio6)
    await bot.send_audio(message.chat.id, audio=audio7)
    await bot.send_audio(message.chat.id, audio=audio8)
    await bot.send_audio(message.chat.id, audio=audio9)
    await bot.send_audio(message.chat.id, audio=audio10)



#video
@dp.message_handler(commands=['video'])
async def video(message: types.Message):
    videos = [
        "video/#мотивация#лучшее мотивация.mp4",
        "video/Bro’s Valid Right.mp4",
        "video/видео со смыслом.mp4",
        "video/Грустное видео . Сильные слова со смыслом.mp4",
        "video/Грустное видео со смыслом! О жизни, о любви.mp4",

        "video/Грустное видео со смыслом, люби и будь любимым.mp4",
        "video/Грустные видео, со смыслом, до слёз 😭_Про любовь душевные слова про любовь💔.mp4",
        "video/Мотивация. Действуй здесь и сейчас! #мотивация #действия #рекомендации #поверьвс.mp4",
        "video/СЛОВА СО СМЫСЛОМ !!! МОТИВАЦИЯ ДЛЯ ЖИЗНИ !!!.mp4",
        "video/Цени каждую секундку, каждый миг! Задумайтесь.mp4",
    ]
    video = open(random.choice(videos), 'rb')
    await message.reply(f"Подождите идет загруска видео!")
    await bot.send_video(message.chat.id, video=video)

#motivationVideo
@dp.message_handler(commands=['motivationVideo'])
async def video(message: types.Message):
    videos = [
        "video/motivation/Живи настоящим! Мотивации #живисейчас #рекомендации #поверьвсебя #мотивация.mp4",
        "video/motivation/Мотивация. Не Сдавайся. #мотивация #поверьвсебя #действия #рекомендации.mp4",
        "video/motivation/Мотивация. У тебя всё получится! #поверьвсебя #действия #саморазвитие.mp4",
        "video/motivation/Мотивация. У тебя всё получится! Действуй. #поверьвсебя #действия #саморазвитие .mp4",
        "video/motivation/Мотивация на действие. Успех. #действия #саморазвитие #успех #поверьвсебя #мышле.mp4",
        "video/motivation/Мотивация на действие.Полю себя! #действия #саморазвитие #поверьвсебя #самосовер.mp4",
    ]
    video = open(random.choice(videos), 'rb')
    await message.reply(f"Подождите идет загруска видео!")
    await bot.send_video(message.chat.id, video=video)

#Вопрос 1
@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next LVL", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "1.Сколько времени росли динозавры?"
    answers = [
        "2 года",
        "Десятки лет",
        "3000 лет",
        "777 лет",
        "МНОГО ЛЕТ"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup=markup
    )

#Вопрос 2
@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Next LVL", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "2.Почему спички называют шведскими?"
    answers = [
        "Полноценный Софистика",
        "Их изобрел швед",
        "Зазвенеть Свояченица",
        "Бабуши Кораблестроитель",
        "Отгореть Призер"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 3
@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Next LVL", callback_data='button_call_3')
    markup.add(button_call_3)

    question = "3.Какова природа икоты?"
    answers = [
        "Наискось Рентгенов",
        "икота возникает за счет сокращения дыхательных мышц",
        "Случайное слово",
        "Бинтовать Лениться",
        "Одолжить Оттенок"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 4
@dp.callback_query_handler(lambda call: call.data == "button_call_3")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("Next LVL", callback_data='button_call_4')
    markup.add(button_call_4)

    question = "4.Как МКС уклоняется от метеорных потоков?"
    answers = [
        "Горшечник Тревога",
        "Никак",
        "Киловатт Простонародье",
        "Лапочка Меркантилизм",
        "Кубовый Мотыль"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 5
@dp.callback_query_handler(lambda call: call.data == "button_call_4")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Next LVL", callback_data='button_call_5')
    markup.add(button_call_5)

    question = "5.Сколько золота в золотой олимпийской медали?"
    answers = [
        "Дальнейший Электродинамика",
        "По стандарту-6 граммов.",
        "Гранатометчик Штаб-квартира",
        "Борение Обвеситься",
        "Гомерический Лощина"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 6
@dp.callback_query_handler(lambda call: call.data == "button_call_5")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_6 = InlineKeyboardButton("Next LVL", callback_data='button_call_6')
    markup.add(button_call_6)

    question = "6.Что значит «дубина стоеросовая»?"
    answers = [
        "Малайцы Присасывание",
        "То же, что неотесанная",
        "Молодогвардеец Поджаристый",
        "Скопидомничать Фтизиатрия",
        "Аппаратчик Мастодонт"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 7
@dp.callback_query_handler(lambda call: call.data == "button_call_6")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_7 = InlineKeyboardButton("Next LVL", callback_data='button_call_7')
    markup.add(button_call_7)

    question = "7.Когда погаснет Солнце?"
    answers = [
        "Мирянин Подсинивать",
        "Приблизительно через 5 миллиардов лет",
        "Атеизм Сложиться",
        "Площадь Усидеть",
        "Несуразный Освоить"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 8
@dp.callback_query_handler(lambda call: call.data == "button_call_7")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_8 = InlineKeyboardButton("Next LVL", callback_data='button_call_8')
    markup.add(button_call_8)

    question = "8.Можно ли китайскими или японскими иероглифами написать русское имя?"
    answers = [
        "Не знаю",
        "Можно, но чаще приблизительно",
        "Наверное",
        "НАРУТОООО",
        "РИМУРУ"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 9
@dp.callback_query_handler(lambda call: call.data == "button_call_8")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_9 = InlineKeyboardButton("Next LVL", callback_data='button_call_9')
    markup.add(button_call_9)

    question = "9.Бывает ли у человека два сердца?"
    answers = [
        "Завзятый Разжаться",
        "Да, хотя и крайне редко",
        "Пробег Сионизм",
        "Наивный Портвейн",
        "Перекраивать Санировать"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 10
@dp.callback_query_handler(lambda call: call.data == "button_call_9")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_10 = InlineKeyboardButton("Next LVL", callback_data='button_call_10')
    markup.add(button_call_10)

    question = "10.Почему для младенцев мужского пола традиционно выбирают одежду голубого цвета, а для новорожденных девочек — розового?"
    answers = [
        "Академический Распутье Тонкопряха",
        "голубая одежда была дешевой формой страховки",
        "Концертмейстер Лыко Пожелать",
        "Выковырять Ростбиф Теннис",
        "Аромат Нагишом Накрутить"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 11
@dp.callback_query_handler(lambda call: call.data == "button_call_10")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_11 = InlineKeyboardButton("Next LVL", callback_data='button_call_11')
    markup.add(button_call_11)

    question = "11.Почему лоси сбрасывают рога?"
    answers = [
        "Карточка Трущоба Фактография",
        "За ненадобностью",
        "Астра Корнеплод Рождаемость",
        "Апаш Всколыхнуться Подстежка",
        "Коррупция Рассердиться Состязание"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 12
@dp.callback_query_handler(lambda call: call.data == "button_call_11")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_12 = InlineKeyboardButton("Next LVL", callback_data='button_call_12')
    markup.add(button_call_12)

    question = "12.Как возникли Гималаи?"
    answers = [
        "Девятнадцать Дождаться Кипяченый",
        "200 миллионов лет назад — Пангею",
        "Огнестрельный Откинуть",
        "Лазурный Экспансивный",
        "Курносый Плошка"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 13
@dp.callback_query_handler(lambda call: call.data == "button_call_12")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_13 = InlineKeyboardButton("Next LVL", callback_data='button_call_13')
    markup.add(button_call_13)

    question = "13.Кто создал борьбу самбо?"
    answers = [
        "Выгнуться Чалка",
        "В 1920-е году Виктор Спиридонов",
        "Алебастр Коллеж",
        "Клептоман Маркетинг",
        "Жевать Стахановец"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 14
@dp.callback_query_handler(lambda call: call.data == "button_call_13")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_14 = InlineKeyboardButton("Next LVL", callback_data='button_call_14')
    markup.add(button_call_14)

    question = "14.Зачем на нефтяных вышках горит огонь?"
    answers = [
        "Доминион Замириться",
        "Это сгорает попутный нефтяной газ",
        "Ворваться Фарисей",
        "Наглазник Отколупать",
        "Одержимый Проперчить"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 15
@dp.callback_query_handler(lambda call: call.data == "button_call_14")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_15 = InlineKeyboardButton("Next LVL", callback_data='button_call_15')
    markup.add(button_call_15)

    question = "15.Далеко ли улетают надутые гелием шарики?"
    answers = [
        "Вымышленный Фиглярить",
        "На тысячи километров",
        "Досадовать Планерка",
        "Назади Опереть",
        "Вольнонаемный Перекраситься"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 16
@dp.callback_query_handler(lambda call: call.data == "button_call_15")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_16 = InlineKeyboardButton("Next LVL", callback_data='button_call_16')
    markup.add(button_call_16)

    question = "16.Как горные козлы держатся на отвесных скалах?"
    answers = [
        "Гладь Жулик",
        "За счет скальных неровностей",
        "Белеть Отъезд",
        "Восторжествовать Нынешний",
        "Прикорнуть Употребительный"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 17
@dp.callback_query_handler(lambda call: call.data == "button_call_16")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_17 = InlineKeyboardButton("Next LVL", callback_data='button_call_17')
    markup.add(button_call_17)

    question = "17.Правда ли,что новорождённые видят мир перевёрнутым?"
    answers = [
        "Жульничать Пюре",
        "Они его вообще почти не видят",
        "Батрачество Капсула",
        "Непримиримый Приказчик",
        "Разукомплектовать Упрочнить"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 18
@dp.callback_query_handler(lambda call: call.data == "button_call_17")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_18 = InlineKeyboardButton("Next LVL", callback_data='button_call_18')
    markup.add(button_call_18)

    question = "18.Почему вода, состоящая из кислорода и водорода, не горит и не взрывается?"
    answers = [
        "Испражняться Прорвать",
        "Потому что она и есть продукт горения",
        "Биолог Инструментовка",
        "Копаться Протекционист",
        "Путаный Умощнить"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 19
@dp.callback_query_handler(lambda call: call.data == "button_call_18")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_19 = InlineKeyboardButton("Next LVL", callback_data='button_call_19')
    markup.add(button_call_19)

    question = "19.Почему Дмитрий Менделеев не получил Нобелевскую премию?"
    answers = [
        "Отрешиться Сформироваться",
        "Можно сказать,не успел",
        "Сиротеть Шелковинка",
        "Гетман Паразит",
        "Аферист Семениться"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 20
@dp.callback_query_handler(lambda call: call.data == "button_call_19")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_20 = InlineKeyboardButton("Next LVL", callback_data='button_call_20')
    markup.add(button_call_20)

    question = "20.Когда появился марш «Прощание славянки»?"
    answers = [
        "Данный Светотехник",
        "В 1912 году",
        "Благотворный Гормя",
        "В 1920 году",
        "Дуршлаг Сохнуть"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 21
@dp.callback_query_handler(lambda call: call.data == "button_call_20")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_21 = InlineKeyboardButton("Next LVL", callback_data='button_call_21')
    markup.add(button_call_21)

    question = "21.Если большую часть атома занимает пустота, почему предметы не проходят сквозь друг друга?"
    answers = [
        "Намалывать Подсидеть",
        "Электронные облака не пропускают друг друга",
        "Отвязаться Счетверить",
        "Арка Где",
        "Кандидатура Тори"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 22
@dp.callback_query_handler(lambda call: call.data == "button_call_21")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_22 = InlineKeyboardButton("Next LVL", callback_data='button_call_22')
    markup.add(button_call_22)

    question = "22.Какой инженерный проект считается самым масштабным?"
    answers = [
        "Горечь Нуждаться",
        "Гигантскому Водопроводу от Ливии до Китая",
        "Облачный Сушиться",
        "Вечереть Питекантроп",
        "Замышляться Торгпред"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 23
@dp.callback_query_handler(lambda call: call.data == "button_call_22")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_23 = InlineKeyboardButton("Next LVL", callback_data='button_call_23')
    markup.add(button_call_23)

    question = "23.Почему Вселенная заполнена веществом почти однородно?"
    answers = [
        "Запеть Отчасти",
        "Потому что вещество расширялось вместе с пространством",
        "Взборонить Упреть",
        "Наслышаться Просцениум",
        "Откачнуть Оцепление"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 24
@dp.callback_query_handler(lambda call: call.data == "button_call_23")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_24 = InlineKeyboardButton("Next LVL", callback_data='button_call_24')
    markup.add(button_call_24)

    question = "24.Бывает ли животным скучно?"
    answers = [
        "Атрибут Попудрить",
        "Да как и людям",
        "Инфраструктура Разбрюзжаться",
        "Дамба Навернуться",
        "Ерник Комета"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 25
@dp.callback_query_handler(lambda call: call.data == "button_call_24")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_25 = InlineKeyboardButton("Next LVL", callback_data='button_call_25')
    markup.add(button_call_25)

    question = "25.Может ли «насытиться» чёрная дыра?"
    answers = [
        "Минута Штыковать",
        "Не может",
        "Пирожник Траверз",
        "Кал Немного",
        "Заботиться Иглотерапия"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 26
@dp.callback_query_handler(lambda call: call.data == "button_call_25")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_26 = InlineKeyboardButton("Next LVL", callback_data='button_call_26')
    markup.add(button_call_26)

    question = "26.Почему в Барселоне все такси черно-желтого цвета?"
    answers = [
        "Нападки Несомненный",
        "черный — цвет траура, и желтый — цвет позора",
        "Внешний Кворум",
        "Кабарга Плафон",
        "Заснятый Соборность"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
        reply_markup = markup
    )

#Вопрос 27
@dp.callback_query_handler(lambda call: call.data == "button_call_26")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_27 = InlineKeyboardButton("Next LVL", callback_data='button_call_27')
    markup.add(button_call_27)

    question = "27.Почему Нидерланды называют Голландией?"
    answers = [
        "Засидеть Моча",
        "имя носит только одна из провинций, а не вся страна",
        "Спокойный Упомянуть",
        "Пенопласт Подпираться",
        "Полюбоваться Совместный"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой ты че?",
    )



@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        # await bot.send_message(message.chat.id, int(message.text) * int(message.text))
        await message.reply(int(message.text) * int(message.text))
    else:
        await message.reply(message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)