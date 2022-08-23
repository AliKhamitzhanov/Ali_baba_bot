import sqlite3
import random

from config import bot


# CRUD


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS ali_menu"
               "(photo_dish TEXT, name_dish TEXT PRIMARY KEY, description_dish TEXT, price_dish INTEGER)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO ali_menu VALUES"
                       "(?, ?, ?, ?)",
                       tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM ali_menu").fetchall()
    random_dish = random.choice(result)
    await bot.send_photo(message.from_user.id, random_dish[0],
                         caption=f"name_dish: {random_dish[1]}\n"
                                 f"description_dish: {random_dish[2]}\n"
                                 f"price_dish: {random_dish[3]} $\n")

async def sql_command_all():
    return cursor.execute("SELECT * FROM ali_menu").fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM ali_menu WHERE name_dish == ?", (id,))
    db.commit()