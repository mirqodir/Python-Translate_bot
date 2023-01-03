import logging
from aiogram import Bot, Dispatcher, executor, types
from config import *
from buttons import *
from aiogram.types import Message,CallbackQuery
from googletrans import Translator

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
translator = Translator()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    javob = f"*Assalomu aleykum {message.from_user.first_name}*"
    javob += "\n*Tarjima qilomoqchi bo'lgan so'z yoki matn kiriting:*"
    await message.reply(javob,parse_mode='markdown')



@dp.message_handler()
async def tarjima_funk(message: types.Message):
    global msg
    msg = message.text
    await message.answer("*Tilni tanlang*",reply_markup=til,parse_mode='markdown')


#english
@dp.callback_query_handler(text='en')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(msg,dest='en')
    await call.message.answer(res.text)
#rus
@dp.callback_query_handler(text='ru')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(msg,dest='ru')
    await call.message.answer(res.text)

#arabic
@dp.callback_query_handler(text='ar')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(msg,dest='ar')
    await call.message.answer(res.text)


#uz
@dp.callback_query_handler(text='uz')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(msg,dest='uz')
    await call.message.answer(res.text)


#french
@dp.callback_query_handler(text='fr')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(msg,dest='fr')
    await call.message.answer(res.text)

#kor
@dp.callback_query_handler(text='kor')
async def til_tanlash(call:CallbackQuery):
    res = translator.translate(msg,dest='ko')
    await call.message.answer(res.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)