from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz_easy_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_easy_call_2 = InlineKeyboardButton("NEXT", callback_data='button_easy_call_2')
    markup.add(button_easy_call_2)

    question = "Вычислите 35-56=?"
    answers = [
        "-19",
        "-23",
        "-21",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )

async def quiz_easy_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_easy_call_3 = InlineKeyboardButton("NEXT", callback_data='button_easy_call_3')
    markup.add(button_easy_call_3)

    question = "Какое число больше: -9453273 или -9453272?"
    answers = [
        "-9453273",
        "-9453272"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )

async def quiz_easy_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_easy_call_4 = InlineKeyboardButton("NEXT", callback_data='button_easy_call_4')
    markup.add(button_easy_call_4)

    question = "Сколько целых раз в 811 вмещается 75?"
    answers = [
        "9",
        "10",
        "11"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )

async def quiz_easy_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_easy_call_5 = InlineKeyboardButton("NEXT", callback_data='button_easy_call_5')
    markup.add(button_easy_call_5)

    question = "2Х+4+Х=8+Х. Чему равен Х?"
    answers = [
        "1",
        "4",
        "2"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )

async def quiz_easy_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_easy_call_6 = InlineKeyboardButton("NEXT", callback_data='button_easy_call_6')
    markup.add(button_easy_call_6)

    question = "Продолжите последовательность: 3; 5; 6; 8; 9; 11..."
    answers = [
        "15",
        "12",
        "13"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )

async def quiz_easy_7(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_easy_call_7 = InlineKeyboardButton("NEXT", callback_data='button_easy_call_7')
    markup.add(button_easy_call_7)

    question = "Теперь продолжите этот ряд: 18; 27; 36; 45..."
    answers = [
        "54",
        "63",
        "49"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )

async def quiz_easy_8(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_easy_call_8 = InlineKeyboardButton("NEXT", callback_data='button_easy_call_8')
    markup.add(button_easy_call_8)

    question = "101, 112, 131, 415, 161, 718... Что дальше?"
    answers = [
        "192",
        "963",
        "511"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        open_period=60,
        explanation="Ой бой махатся будеш!",
    )


def register_handlers_callback_easy(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_easy_2, lambda call: call.data == "button_easy_call_1")
    dp.register_callback_query_handler(quiz_easy_3, lambda call: call.data == "button_easy_call_2")
    dp.register_callback_query_handler(quiz_easy_4, lambda call: call.data == "button_easy_call_3")
    dp.register_callback_query_handler(quiz_easy_5, lambda call: call.data == "button_easy_call_4")
    dp.register_callback_query_handler(quiz_easy_6, lambda call: call.data == "button_easy_call_5")
    dp.register_callback_query_handler(quiz_easy_7, lambda call: call.data == "button_easy_call_6")
    dp.register_callback_query_handler(quiz_easy_8, lambda call: call.data == "button_easy_call_7")
