from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
import random
from keyboard.client_kb import start_markup
from perser.doramy import parserDoramy
import time


async def menu(message: types.Message):
    await bot.send_message(message.chat.id, f"СИСТЕМА ГАЧИМУЧИ ОТКРЫЛАСЬ!\n"
                                            f"Добро пожаловать {message.from_user.full_name}", reply_markup=start_markup)


async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда должна быть ответом на сообщение!")
    else:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


async def dice(message: types.Message):
    if message.chat.type != "private":
        await bot.send_message(message.chat.id, f"Выбор БОТА:")
        bot_choice = await bot.send_dice(message.chat.id, emoji="🎲")
        await bot.send_message(message.chat.id, f"Выбор {message.from_user.first_name}:")
        user_choice = await bot.send_dice(message.chat.id, emoji="🎲")
        time.sleep(4)
        bot_answer = bot_choice.dice.value
        user_answer = user_choice.dice.value
        if bot_answer > user_answer:
            await bot.send_message(message.chat.id, f"{message.from_user.first_name} проиграл БОТУ!")
        elif bot_answer < user_answer:
            await bot.send_message(message.chat.id, f"{message.from_user.first_name} выиграл БОТА!")
        elif bot_answer == user_answer:
            await bot.send_message(message.chat.id, f"Ничья победила дружба (>_<)")
    else:
        await message.reply("Пиши в группе путник!")


# quiz
async def quiz(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton(text="Легкие вопросы", callback_data="button_easy_call_1"),
        types.InlineKeyboardButton(text="Средние вопросы", callback_data="button_medium_call_1"),
        types.InlineKeyboardButton(text="Сложные вопросы", callback_data="button_hard_call_1")
    )

    await message.answer("Выбери сложность вопросов", reply_markup=markup)


# quiz_easy
async def quiz_easy(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_easy_call_1 = InlineKeyboardButton("NEXT", callback_data='button_easy_call_1')
    markup.add(button_easy_call_1)

    question = "Какое число лишнее: 1, 3, 5, 6, 7?"
    answers = [
        "7",
        "6",
        "1",
        "3",
        "5"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )


# quiz_medium
async def quiz_medium(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_medium_call_1 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_1')
    markup.add(button_medium_call_1)

    question = "Совокупность всех объектов, изменение свойств которых влияет на системы, а также тух объектов, чьи свойства меняются в результате " \
               "поведения системы, это: "
    answers = [
        "среда",
        "подсистема",
        "компоненты"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )


# quiz_hard
async def quiz_hard(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_hard_call_1 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_1')
    markup.add(button_hard_call_1)

    question = "Признаки открытой экономики:"
    answers = [
        "экспорт превышает импорт",
        "внешнеторговый оборот достигает 25% от ВВП",
        "импорт превышает экспорт",
        "внешнеторговый оборот достигает 10% от ВВП"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )


# mem
# async def mem(message: types.Message):
#     photos = [
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image1.jpg",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image2.jpg",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image3.jpg",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image4.jpg",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image5.jpg",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image6.jpg",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image7.jpg",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image8.jpg",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image9.jpg",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/imges/image10.jpg",
#     ]
#     img = open(random.choice(photos), 'rb')
#     await message.reply(f"Жди мем(>_<)")
#     await bot.send_photo(message.chat.id, photo=img)


# music
# async def music(message: types.Message):
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(
#         types.InlineKeyboardButton(text="1", callback_data="music_1"),
#         types.InlineKeyboardButton(text="2", callback_data="music_2"),
#         types.InlineKeyboardButton(text="3", callback_data="music_3"),
#         types.InlineKeyboardButton(text="4", callback_data="music_4"),
#         types.InlineKeyboardButton(text="5", callback_data="music_5"),
#         types.InlineKeyboardButton(text="6", callback_data="music_6"),
#         types.InlineKeyboardButton(text="7", callback_data="music_7"),
#         types.InlineKeyboardButton(text="8", callback_data="music_8"),
#         types.InlineKeyboardButton(text="9", callback_data="music_9"),
#         types.InlineKeyboardButton(text="10", callback_data="music_10"),
#     )
#
#     await message.answer("Выбери песню которую хочешь послушать)\n"
#                          "1.Ирина Кайратовна, Shiza – Кок ту\n"
#                          "2.instasamka-moja-kiska-dlja-nego-vsegda-gotova\n"
#                          "3.Lil_Nas_X_Jack_Harlow_-_INDUSTRY_BABY\n"
#                          "4.Lizzo_-_About_Damn_Time\n"
#                          "5.Melanie_Martinez_-_Cake\n"
#                          "6.Naruto Shippuden OST — Opening №1\n"
#                          "7.opening_1_sezona_-_Klinok_rassekayushhijj_demonov\n"
#                          "8.OST_Naruto_shippuden_Ikimono-gakari_-_Blue_Bird\n"
#                          "9.Vance_Joy_-_Missing_Piece\n"
#                          "10.Vance_Joy_-_Riptide\n", reply_markup=keyboard, )


# video
# async def video(message: types.Message):
#     videos = [
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/#мотивация#лучшее мотивация.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/Bro’s Valid Right.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/видео со смыслом.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/Грустное видео . Сильные слова со смыслом.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/Грустное видео со смыслом! О жизни, о любви.mp4",
#
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/Грустное видео со смыслом, люби и будь любимым.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/Грустные видео, со смыслом, до слёз 😭_Про любовь душевные слова про любовь💔.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/Мотивация. Действуй здесь и сейчас! #мотивация #действия #рекомендации #поверьвс.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/СЛОВА СО СМЫСЛОМ !!! МОТИВАЦИЯ ДЛЯ ЖИЗНИ !!!.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/Цени каждую секундку, каждый миг! Задумайтесь.mp4",
#     ]
#     video = open(random.choice(videos), 'rb')
#     await message.reply(f"Подождите идет загруска видео!")
#     await bot.send_video(message.chat.id, video=video)


# motivationVideo
# async def motivationVideo(message: types.Message):
#     videos = [
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/motivation/Живи настоящим! Мотивации #живисейчас #рекомендации #поверьвсебя #мотивация.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/motivation/Мотивация. Не Сдавайся. #мотивация #поверьвсебя #действия #рекомендации.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/motivation/Мотивация. У тебя всё получится! #поверьвсебя #действия #саморазвитие.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/motivation/Мотивация. У тебя всё получится! Действуй. #поверьвсебя #действия #саморазвитие .mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/motivation/Мотивация на действие. Успех. #действия #саморазвитие #успех #поверьвсебя #мышле.mp4",
#         "C:/Users/User/PycharmProjects/NAEGYOII/handlers/video/motivation/Мотивация на действие.Полю себя! #действия #саморазвитие #поверьвсебя #самосовер.mp4",
#     ]
#     video = open(random.choice(videos), 'rb')
#     await message.reply(f"Подождите идет загруска видео!")
#     await bot.send_video(message.chat.id, video=video)


async def parser_doramy(message: types.Message):
    data = parserDoramy()
    for item in data:
        await bot.send_message(
            message.from_user.id,
            f"{item['link']}\n\n"
            f"{item['title']}\n"
            f"Автор: {item['authors']}\n\n"
            f"#{item['series']}\n"
            f"#{item['country']}\n"
            f"#{item['year']}\n"
            f"#{item['genre']}\n"
            f"#{item['added']}\n"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(menu, commands=['start'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix=['!'])
    dp.register_message_handler(dice, commands=['dice'])
    dp.register_message_handler(quiz, commands=['quiz'])
    dp.register_message_handler(quiz_easy, commands=['quizEasy'])
    dp.register_message_handler(quiz_medium, commands=['quizMedium'])
    dp.register_message_handler(quiz_hard, commands=['quizHard'])
    # dp.register_message_handler(mem, commands=['mem'])
    # dp.register_message_handler(music, commands=['music'])
    # dp.register_message_handler(video, commands=['video'])
    # dp.register_message_handler(motivationVideo, commands=['motivationVideo'])
    dp.register_message_handler(parser_doramy, commands=['doramy'])
