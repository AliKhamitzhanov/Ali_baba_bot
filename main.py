from aiogram.utils import executor
from config import dp, URL, bot
import logging
from handlers import client, keyboard_music, admin, extra, fsm_menu, notification
from handlers import callback_easy, callback_medium, callback_hard, inline
from database import bot_db
import asyncio

from decouple import config


async def on_start(_):
    await bot.set_webhook(URL)
    asyncio.create_task(notification.scheduler())
    bot_db.sql_create()


async def on_shutdown(dp):
    await bot.delete_webhook()


client.register_handlers_client(dp)
keyboard_music.register_handlers_keyboard(dp)
callback_easy.register_handlers_callback_easy(dp)
callback_medium.register_handlers_callback_medium(dp)
callback_hard.register_handlers_callback_hard(dp)

notification.register_handler_notification(dp)

fsm_menu.register_handlers_fsm_menu(dp)
admin.register_handlers_admin(dp)

inline.register_handler_inline(dp)

extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # executor.start_polling(dp, skip_updates=True, on_startup=on_start)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_start,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", cast=int)
    )

# nice11

