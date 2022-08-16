from aiogram import types, Dispatcher
from config import bot
from config import ADMIN
import random


async def game(message: types.Message):
    games = ["🎯", "🎳", "🎲", "🎰", "🏀","⚽"]
    games_random = random.choice(games)
    if message.text == "game":
        if message.chat.type != "private":
            if message.from_user.id in ADMIN:
                await bot.send_dice(message.chat.id, emoji=games_random)
            else:
                await message.reply("Ой бой ты кто?\n"
                                    "Ты не мой Создатель (-_-)")
        else:
            await message.reply("Пиши в группе путник!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=["ame"], commands_prefix="g")