import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text=f"Система Ali_Ba_Ba активирована!\n"
                                                 f"Добро пажаловать{message.from_user.full_name}\n\n"
                                                 f"«Как смешны требования людей курящих, пьющих, объедающихся, не работающих и превращающих ночь в день о том, чтобы доктор сделал их здоровыми, несмотря на их нездоровый образ жизни», — Л.Н. Толстой.")


async def good_morning_dragons():
    await bot.send_message(chat_id=chat_id, text=f"Доброе утро воин\n"
                                                 f"Удачного дня =)"
                                                 f"https://www.youtube.com/watch?v=tkDtIf0Oozg")


async def go_to_sleep_dragons():
    await bot.send_message(chat_id=chat_id, text="Воин пора ложиться спать)\n"
                                                 "https://www.youtube.com/watch?v=NZFAkLphctk")


async def write_to_adele():
    await bot.send_message(chat_id=chat_id, text="Напиши будущей жене)\n"
                                                 "@naegyoii")


async def gyma_namaz():
    await bot.send_message(chat_id=chat_id, text="Жума намаз убактысы болду")


async def scheduler():
    aioschedule.every().day.at("6:00").do(good_morning_dragons)
    aioschedule.every().day.at("21:30").do(go_to_sleep_dragons)
    aioschedule.every().friday.at("12:00").do(gyma_namaz)
    aioschedule.every().day.at("4:00").do(write_to_adele)
    aioschedule.every().day.at("8:00").do(write_to_adele)
    aioschedule.every().day.at("12:00").do(write_to_adele)
    aioschedule.every().day.at("16:00").do(write_to_adele)
    aioschedule.every().day.at("16:10").do(write_to_adele)
    aioschedule.every().day.at("20:00").do(write_to_adele)
    aioschedule.every().day.at("00:00").do(write_to_adele)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(3.14)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: "Я воин дракона" in word.text)
