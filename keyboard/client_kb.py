from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# mem = KeyboardButton("/mem")
# music = KeyboardButton("/music")
# video = KeyboardButton("/video")
# motivationVideo = KeyboardButton("/motivationVideo")
game = KeyboardButton("game")
dice = KeyboardButton("/dice")
quiz = KeyboardButton("/quiz")
doramy = KeyboardButton("/doramy")
ali_menu = KeyboardButton("/ali_menu")
delelt = KeyboardButton("/del")
notifik = KeyboardButton("Я воин дракона")

start_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                   one_time_keyboard=True)

start_markup.row(game, dice, quiz, doramy, ali_menu, delelt, notifik)

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