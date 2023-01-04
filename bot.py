import asyncio
import logging
from aiogram import Bot, Dispatcher, types

logging.basicConfig(level=logging.INFO)
bot=Bot(token="5287719198:AAE3e5ZATQJXiCJXJ0gwMy5TUn8CrXm_4co")
dp=Dispatcher()

@dp.message(commands=['start',"answer"])
async def cmd_start(message: types.Message):
    await message.answer('Это простой ответ')

async def cmd_reply(message: types.Message):
    await message.answer('Это ответ с "ответом"')

async  def main():
    dp.message.register(cmd_reply, commands=['reply'])
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())