from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

import asyncio
import keyboards as kb

from config import token

bot = Bot(token = token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
  await message.answer(f'Добро пожаловать в онлайн-магазин {message.from_user.first_name}!\nв сообщении ниже вы можете выбрать товар', reply_markup=kb.main)
  
@dp.message(F.text == 'Товары')
async def direction(message: Message):
    await message.answer('У нас имеются 3 направление по кнопкам ниже', reply_markup=kb.setting)

@dp.callback_query(F.data == 't_shirt')
async def t_shirt(query):
    await query.message.answer('Футболка\nScuderia Ferrari Desert Sun\n$50.00')
    
@dp.callback_query(F.data == 'sneakers')
async def sneakers(query):
    await query.message.answer('Кроссовка\nAll-Pro NITRO™ Elite\n$250.00')
  
@dp.callback_query(F.data == 'pants')
async def pants(query):
    await query.message.answer('Штаны\nPUMA x THE BROOKLYN CIRCUS\n$130.00')
  
@dp.callback_query(F.data == 'sweater')
async def sweater(query):
    await query.message.answer('Свитер\nVillage Wear\n$75.00')

  
async def main():
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Вы отключились от бота!")
  