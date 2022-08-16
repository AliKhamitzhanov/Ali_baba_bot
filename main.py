from aiogram.utils import executor
from config import dp
import logging
from handlers import client, keyboard, admin, extra
from handlers import callback_easy, callback_medium, callback_hard

client.register_handlers_client(dp)
keyboard.register_handlers_keyboard(dp)
callback_easy.register_handlers_callback_easy(dp)
callback_medium.register_handlers_callback_medium(dp)
callback_hard.register_handlers_callback_hard(dp)
admin.register_handlers_admin(dp)


extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)