from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import bot, ADMIN
from keyboard.client_kb import cancel_markup, meals
from database import bot_db


class FSMAdmin(StatesGroup):  # Finite State Machine
    photo_dish = State()
    meals_dish = State()
    name_dish = State()
    description_dish = State()
    price_dish = State()

async def fsm_start_menu(message: types.Message):
    if message.from_user.id in ADMIN:
        await FSMAdmin.photo_dish.set()
        await message.answer(f"Добро пожаловать {message.from_user.full_name} (>_<)\n"
                             f"Скиньте фото блюда(>_<):",
                             reply_markup=cancel_markup)
    else:
        await message.reply("Это програма только для технологов общественного питания!\n(-_-)")


async def load_photo_dish(message: types.Message, state: FSMContext):
    async with state.proxy() as ali_menu:
        ali_menu['photo_dish'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Прием пищи:", reply_markup=meals)


async def load_meals_dish(message: types.Message, state: FSMContext):

    async with state.proxy() as ali_menu:
        meals = ["Завтрак", "Ланч", "Обед", "Полдник", "Ужин"]
        if message.text in meals:
            ali_menu['meals_dish'] = message.text
            await FSMAdmin.next()
            await message.answer("Напишите название блюда(>_<):", reply_markup=cancel_markup)
        else:
            await message.reply('Ой бой это прием пищи а не чушь (-_-)')


async def load_name_dish(message: types.Message, state: FSMContext):
    async with state.proxy() as ali_menu:
        ali_menu['name_dish'] = message.text
    await FSMAdmin.next()
    await message.answer('Опишите вашего блюда(>_<):')


async def load_description_dish(message: types.Message, state: FSMContext):
    async with state.proxy() as ali_menu:
        if len(message.text) < 10 and len(message.text) < 50:
            await message.reply('Ваше описание должно состоять < 10 символов и > 50')
        else:
            ali_menu['description_dish'] = message.text
            await FSMAdmin.next()
            await message.answer('Цена вашего блюда в сомах(>_<):')


async def load_price_dish(message: types.Message, state: FSMContext):
    try:
        if (int(message.text)) <= 20000:
            async with state.proxy() as ali_menu:
                ali_menu['price_dish'] = (int(message.text)) / 80
                await bot.send_photo(message.chat.id, ali_menu['photo_dish'],
                                     caption=f"Прием пищи: {ali_menu['meals_dish']}\n"
                                             f"Название вашего блюда: {ali_menu['name_dish']}\n"
                                             f"Описание вашего блюда: {ali_menu['description_dish']}\n"
                                             f"Цена вашего блюда: {ali_menu['price_dish']} $")
            await bot_db.sql_command_insert(state)
            await state.finish()
            await message.answer(f"На этом все, технолог общественного питания {message.from_user.first_name}")
        else:
            await bot.send_message(message.chat.id, " Э Ой бой ты так цену не задирай мы же простой народ(^_^)")
    except ValueError:
        await bot.send_message(message.chat.id, "Ой бой ты че на бабки разводиш(*_*)\n"
                                                     "Вводите только цифры")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Ой бой регистрация отменена гой.")


async def delete_ali_menu(message: types.Message):
    if message.from_user.id in ADMIN and message.chat.type == "private":
        dishes = await bot_db.sql_command_all()
        for dish in dishes:
            await bot.send_photo(message.from_user.id, dish[0],
                                 caption=f"meals_dish: {dish[1]}\n"
                                         f"name_dish: {dish[2]}\n"
                                         f"description_dish: {dish[3]}\n"
                                         f"price_dish: {dish[4]}\n",
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(
                                         f"Delete: {dish[2]}",
                                         callback_data=f"Delete {dish[2]}"
                                     )
                                 )
                                 )
    else:
        await message.reply("Ой бой ты кто?\n"
                            "Ты не мой Создатель (-_-)")


async def complete_delete_dish(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace('Delete ', ""))
    await call.answer(text="Ой ты блюдо уничтожил.", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsm_menu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands='Отменить регестарцию')
    dp.register_message_handler(cancel_registration, Text(equals='Отменить регестарцию', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start_menu, commands=['ali_menu'])
    dp.register_message_handler(load_photo_dish, state=FSMAdmin.photo_dish,
                                content_types=['photo'])
    dp.register_message_handler(load_meals_dish, state=FSMAdmin.meals_dish)
    dp.register_message_handler(load_name_dish, state=FSMAdmin.name_dish)
    dp.register_message_handler(load_description_dish, state=FSMAdmin.description_dish)
    dp.register_message_handler(load_price_dish, state=FSMAdmin.price_dish)
    dp.register_message_handler(delete_ali_menu, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete_dish,
        lambda call: call.data and call.data.startswith("Delete ")
    )
