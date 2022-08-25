from aiogram import types, Dispatcher
from config import bot



async def music_1(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/Ирина Кайратовна, Shiza – Кок ту.mp3", 'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


async def music_2(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/instasamka-moja-kiska-dlja-nego-vsegda-gotova_(kztrack.kz).mp3", 'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


async def music_3(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/Lil_Nas_X_Jack_Harlow_-_INDUSTRY_BABY_73061759.mp3",'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


async def music_4(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/Lizzo_-_About_Damn_Time_74115343.mp3", 'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


async def music_5(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/Melanie_Martinez_-_Cake_48195644.mp3", 'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


async def music_6(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/Naruto Shippuden OST — Opening №1 (www.lightaudio.ru).mp3", 'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


async def music_7(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/opening_1_sezona_-_Klinok_rassekayushhijj_demonov_65423151.mp3", 'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


async def music_8(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/OST_Naruto_shippuden_Ikimono-gakari_-_Blue_Bird_OP3_62967143.mp3", 'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


async def music_9(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/Vance_Joy_-_Missing_Piece_73152511.mp3", 'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


async def music_10(call: types.CallbackQuery):
    audio = open("C:/Users/User/PycharmProjects/NAEGYOII/music/Vance_Joy_-_Riptide_47960565.mp3", 'rb')
    await bot.send_audio(call.message.chat.id, audio=audio)


def register_handlers_keyboard(dp: Dispatcher):
    dp.register_callback_query_handler(music_1, lambda call: call.data == "music_1")
    dp.register_callback_query_handler(music_2, lambda call: call.data == "music_2")
    dp.register_callback_query_handler(music_3, lambda call: call.data == "music_3")
    dp.register_callback_query_handler(music_4, lambda call: call.data == "music_4")
    dp.register_callback_query_handler(music_5, lambda call: call.data == "music_5")
    dp.register_callback_query_handler(music_6, lambda call: call.data == "music_6")
    dp.register_callback_query_handler(music_7, lambda call: call.data == "music_7")
    dp.register_callback_query_handler(music_8, lambda call: call.data == "music_8")
    dp.register_callback_query_handler(music_9, lambda call: call.data == "music_9")
    dp.register_callback_query_handler(music_10, lambda call: call.data == "music_10")