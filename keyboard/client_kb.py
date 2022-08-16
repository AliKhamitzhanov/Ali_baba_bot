from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

mem = KeyboardButton("/mem")
music = KeyboardButton("/music")
video = KeyboardButton("/video")
motivationVideo = KeyboardButton("/motivation")

start_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)

start_markup.row(mem, music, video, motivationVideo)
