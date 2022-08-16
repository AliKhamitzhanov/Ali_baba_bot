from aiogram import types, Dispatcher
from config import bot

# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        # await bot.send_message(message.chat.id, int(message.text) * int(message.text))
        await message.reply(int(message.text) * int(message.text))
    else:
        await message.reply(message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
