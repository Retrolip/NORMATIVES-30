import asyncio
import psycopg2 as pg
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

API_KEY = ""
TOKEN = "8022931974:AAEH0C10dqGGlEvFochjb6dgBj4jVQN30Dk"

bot = Bot(TOKEN)
dp = Dispatcher()

conn = pg.connect(
    dbname="postgres",
    user="postgres",
    password="suhaylxd2019Z",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    cursor.execute("SELECT title, price FROM course_course")
    infos = cursor.fetchall()

    if infos:
        text = "\n".join([f"{title} — {price} суммов" for title, price in infos])
        await message.answer(text)

    else:
        await message.answer("Курсов нету")


async def main():
    print("🤖 Бот запустился...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
