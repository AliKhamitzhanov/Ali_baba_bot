from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

from config import bot


async def quiz_hard_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_2 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_2')
    markup.add(button_hard_call_2)

    question = "Коэффициент эластичности внешнеторгового оборота по отношению к ВВП показывает:"
    answers = [
        "степень открытости национальной экономики",
        "структуру ВВП",
        "изменение структуры внешнеторгового оборота"
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

async def quiz_hard_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_3 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_3')
    markup.add(button_hard_call_3)

    question = "В развивающихся странах в производстве ВВП доля неформального сектора, бартерных сделок, производства домашних хозяйств, по сравнению с развитыми странами:"
    answers = [
        "больше",
        "меньше"
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

async def quiz_hard_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_4 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_4')
    markup.add(button_hard_call_4)

    question = "Если известны объемы экспорта и импорта страны, то это позволяет вычислить:"
    answers = [
        "экспортную квоту",
        "внешнеторговую квоту",
        "торговый баланс",
        "оборот внешней торговли"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        open_period=60,
        explanation="Ой бой махатся будеш!",
        reply_markup=markup
    )

async def quiz_hard_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_5 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_5')
    markup.add(button_hard_call_5)

    question = "Таможенная пошлина, которая рассчитывается в процентах от таможенной стоимости товара:"
    answers = [
        "специфическая",
        "комбинированная",
        "адвалорная"
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

async def quiz_hard_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_6 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_6')
    markup.add(button_hard_call_6)

    question = "Существенными инструментами защиты внутреннего рынка являются:"
    answers = [
        "экспортные пошлины",
        "импортные квоты",
        "импортные пошлины",
        "экспортные субсидии"
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

async def quiz_hard_7(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_7 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_7')
    markup.add(button_hard_call_7)

    question = "Для поддержания фиксированного валютного курса государство:"
    answers = [
        "использует валютные резервы",
        "вводит ограничения внешней торговли",
        "вводит валютный контроль",
        "повышает налоги"
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

async def quiz_hard_8(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_8 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_8')
    markup.add(button_hard_call_8)

    question = "Если единицы национальной валюты выражаются в иностранной валюте, то это:"
    answers = [
        "прямая котировка",
        "косвенная котировка",
        "кросс-курс",
        "форвард-курс"
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

async def quiz_hard_9(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_9 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_9')
    markup.add(button_hard_call_9)

    question = "Если уровень процентных ставок в стране растет, а в стране иностранной валюты НЕ меняется, то при прочих равных условиях курс национальной валюты:"
    answers = [
        "снижается",
        "растет",
        "не меняется",
        "прогнозировать невозможно"
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

async def quiz_hard_10(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_10 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_10')
    markup.add(button_hard_call_10)

    question = "Если в стране растет пассив торгового баланса, то при прочих равных условиях курс национальной валюты имеет тенденцию:"
    answers = [
        "снижаться",
        "расти",
        "волнообразно изменяться",
        "стабилизироваться на одном уровне"
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

async def quiz_hard_11(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_11 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_11')
    markup.add(button_hard_call_11)

    question = "Если в стране темпы инфляции за три месяца составили 26%, а в стране иностранной валюты 4%, то при прочих равных условиях национальная валюта по отношению к данной иностранной валюте имеет тенденцию:"
    answers = [
        "дорожать",
        "дешеветь",
        "не изменять курс"
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

async def quiz_hard_12(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_12 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_12')
    markup.add(button_hard_call_12)

    question = "Плавающие валютные курсы были узаконены:"
    answers = [
        "Системой золотого стандарта",
        "Бреттон-Вудской валютной системой",
        "Ямайскими соглашениями",
        "на Генуэзской конференции"
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

async def quiz_hard_13(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_13 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_13')
    markup.add(button_hard_call_13)

    question = "Международный валютный фонд был создан решением:"
    answers = [
        "Бреттон-Вудской валютной конференции",
        "Ямайской конференции",
        "Совета Безопасности ООН",
        "Конференции ГАТТ"
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

async def quiz_hard_14(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_14 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_14')
    markup.add(button_hard_call_14)

    question = "При плавающих валютных курсах паритеты определяются:"
    answers = [
        "мировым валютным рынком",
        "решениями правительства",
        "решениями МВФ",
        "национальными Центральными банками"
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

async def quiz_hard_15(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_hard_call_15 = InlineKeyboardButton("NEXT", callback_data='button_hard_call_15')
    markup.add(button_hard_call_15)

    question = "Экономические расчеты между странами упрощаются и удешевляются, снижаются неопределенности и ошибки в принятии решений в сфере международной торговли, снижаются трансакционные издержки – все это происходит при:"
    answers = [
        "фиксированных валютных курсах",
        "плавающих валютных курсах",
        "золотом стандарте"
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

def register_handlers_callback_hard(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_hard_2, lambda call: call.data == "button_hard_call_1")
    dp.register_callback_query_handler(quiz_hard_3, lambda call: call.data == "button_hard_call_2")
    dp.register_callback_query_handler(quiz_hard_4, lambda call: call.data == "button_hard_call_3")
    dp.register_callback_query_handler(quiz_hard_5, lambda call: call.data == "button_hard_call_4")
    dp.register_callback_query_handler(quiz_hard_6, lambda call: call.data == "button_hard_call_5")
    dp.register_callback_query_handler(quiz_hard_7, lambda call: call.data == "button_hard_call_6")
    dp.register_callback_query_handler(quiz_hard_8, lambda call: call.data == "button_hard_call_7")
    dp.register_callback_query_handler(quiz_hard_9, lambda call: call.data == "button_hard_call_8")
    dp.register_callback_query_handler(quiz_hard_10, lambda call: call.data == "button_hard_call_9")
    dp.register_callback_query_handler(quiz_hard_11, lambda call: call.data == "button_hard_call_10")
    dp.register_callback_query_handler(quiz_hard_12, lambda call: call.data == "button_hard_call_11")
    dp.register_callback_query_handler(quiz_hard_13, lambda call: call.data == "button_hard_call_12")
    dp.register_callback_query_handler(quiz_hard_14, lambda call: call.data == "button_hard_call_13")
    dp.register_callback_query_handler(quiz_hard_15, lambda call: call.data == "button_hard_call_14")