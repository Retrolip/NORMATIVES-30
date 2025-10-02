import asyncio
import aiohttp
import psycopg2 as pg
import django
import sys
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from asgiref.sync import sync_to_async

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'normativ.settings')
django.setup()

from course.models import Course

API_KEY = "http://127.0.0.1:8000/api/course/"
TOKEN = "..."

bot = Bot(TOKEN)
dp = Dispatcher()


#
# @sync_to_async
# def get_courses():
#     return list(Course.objects.all())

async def get_courses():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_KEY}") as response:
            return await response.json()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):

    infos = await get_courses()

    print(infos)

async def main():
    print("🤖 Бот запустился...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
