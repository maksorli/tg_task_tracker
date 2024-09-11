import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
import os
from sqlalchemy.orm import Session
from config import engine
from models.models import  TelegramUser
logging.basicConfig(level=logging.INFO)
load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    with Session(engine) as session:
        telegram_user_ids = session.query(TelegramUser.telegram_id).all()
        
        telegram_user_ids = [str(id_tuple[0]) for id_tuple in telegram_user_ids]
        
        telegram_user_ids_str = ', '.join(telegram_user_ids)

        await message.reply(telegram_user_ids_str)

async def cmd_test2(message: types.Message):
    await message.reply("Test 2")
async def main():
    await dp.start_polling(bot)
dp.message.register(cmd_test2, Command("test2"))
if __name__ == "__main__":
    asyncio.run(main())