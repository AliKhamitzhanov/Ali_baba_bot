from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


async def quiz_medium_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_2 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_2')
    markup.add(button_medium_call_2)

    question = "Простейшая, неделимая часть системы, определяемая в зависимости от цели построения и анализа системы:"
    answers = [
        "компонент",
        "наблюдатель",
        "элемент",
        "атом"
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

async def quiz_medium_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_3 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_3')
    markup.add(button_medium_call_3)

    question = "Ограничение системы свободы элементов определяют понятием"
    answers = [
        "критерий",
        "цель",
        "связь",
        "страта"
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

async def quiz_medium_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_4 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_4')
    markup.add(button_medium_call_4)

    question = "Способность системы в отсутствии внешних воздействий сохранять своё состояние сколь угодно долго определяется понятием"
    answers = [
        "устойчивость",
        "развитие",
        "равновесие",
        "поведение"
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

async def quiz_medium_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_5 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_5')
    markup.add(button_medium_call_5)

    question = "Объединение некоторых параметров системы в параметре более высокого уровня - это"
    answers = [
        "синергия",
        "агрегирование",
        "иерархия"
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

async def quiz_medium_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_6 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_6')
    markup.add(button_medium_call_6)

    question = "Уровень иерархической структуры, при которой система представлена в виде взаимодействующих подсистем, называется"
    answers = [
        "стратой",
        "эшелоном",
        "слоем"
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

async def quiz_medium_7(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_7 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_7')
    markup.add(button_medium_call_7)

    question = "Какого вида структуры систем не существует"
    answers = [
        "с произвольными связями",
        "горизонтальной",
        "смешанной",
        "матричной"
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

async def quiz_medium_8(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_8 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_8')
    markup.add(button_medium_call_8)

    question = "Какая из особенностей не является характеристикой развивающихся систем"
    answers = [
        "однонаправленность",
        "нестационарность отдельных параметров",
        "целеобразование",
        "уникальность поведения системы"
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

async def quiz_medium_9(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_9 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_9')
    markup.add(button_medium_call_9)

    question = "Какая закономерность проявляется в системе в появлении у неё новых свойств, отсутствующих у элементов"
    answers = [
        "интегративность",
        "аддитивность",
        "целостность",
        "обособленность"
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

async def quiz_medium_10(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_10 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_10')
    markup.add(button_medium_call_10)

    question = "Коммуникативность относится к группе закономерностей"
    answers = [
        "осуществимости систем",
        "иерархической упорядоченности систем",
        "взаимодействия части и целого",
        "развитие систем"
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

async def quiz_medium_11(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_medium_call_11 = InlineKeyboardButton("NEXT", callback_data='button_medium_call_11')
    markup.add(button_medium_call_11)

    question = "одной из характеристик функционирования системы, определяющейся как способность системы возвращаться в состояние равновесия после того, как она была выведена из этого состояния под влиянием возмущающих воздействий, является"
    answers = [
        "равновесие",
        "устойчивость",
        "развитие",
        "самоорганизация"
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


def register_handlers_callback_medium(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_medium_2, lambda call: call.data == "button_medium_call_1")
    dp.register_callback_query_handler(quiz_medium_3, lambda call: call.data == "button_medium_call_2")
    dp.register_callback_query_handler(quiz_medium_4, lambda call: call.data == "button_medium_call_3")
    dp.register_callback_query_handler(quiz_medium_5, lambda call: call.data == "button_medium_call_4")
    dp.register_callback_query_handler(quiz_medium_6, lambda call: call.data == "button_medium_call_5")
    dp.register_callback_query_handler(quiz_medium_7, lambda call: call.data == "button_medium_call_6")
    dp.register_callback_query_handler(quiz_medium_8, lambda call: call.data == "button_medium_call_7")
    dp.register_callback_query_handler(quiz_medium_9, lambda call: call.data == "button_medium_call_8")
    dp.register_callback_query_handler(quiz_medium_10, lambda call: call.data == "button_medium_call_9")
    dp.register_callback_query_handler(quiz_medium_11, lambda call: call.data == "button_medium_call_10")