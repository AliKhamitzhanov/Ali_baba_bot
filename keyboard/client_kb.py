from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mem = KeyboardButton("/mem")
music = KeyboardButton("/music")
video = KeyboardButton("/video")
motivationVideo = KeyboardButton("/motivation")

start_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)

start_markup.row(mem, music, video, motivationVideo)

cancel_button = KeyboardButton("Отменить регестарцию")
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(cancel_button)


breakfast = KeyboardButton("Завтрак")
lunch = KeyboardButton("Ланч")
obed = KeyboardButton("Обед")
afternoon_tea = KeyboardButton("Полдник")
dinner = KeyboardButton("Ужин")

meals = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).row(breakfast, lunch, obed, afternoon_tea, dinner)