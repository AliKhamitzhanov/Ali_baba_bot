from aiogram.utils import executor
from config import dp
import logging
from handlers import client, keyboard_music, admin, extra, fsm_menu, notification
from handlers import callback_easy, callback_medium, callback_hard
from database import bot_db
import asyncio


async def on_start(_):
    asyncio.create_task(notification.scheduler())
    bot_db.sql_create()


client.register_handlers_client(dp)
keyboard_music.register_handlers_keyboard(dp)
callback_easy.register_handlers_callback_easy(dp)
callback_medium.register_handlers_callback_medium(dp)
callback_hard.register_handlers_callback_hard(dp)

notification.register_handler_notification(dp)

fsm_menu.register_handlers_fsm_menu(dp)
admin.register_handlers_admin(dp)


extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)