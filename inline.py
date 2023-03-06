from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os 

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

answ = dict()

#tugma ssilkasi
urlkb = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='ssilka', url='https://youtube.com')
urlButton2 = InlineKeyboardButton(text='ssilka2', url='https://google.com')
x = [InlineKeyboardButton(text='ssilka3', url='https://google.com'),InlineKeyboardButton(text='ssilka4', url='https://google.com'),\
	InlineKeyboardButton(text='ssilka5', url='https://google.com'),]
urlkb.add(urlButton,urlButton2).row(*x).insert(InlineKeyboardButton(text='ssilka2',url='https://google.com'))

@dp.message_handler(commands=['ssilkalar'])
async def url_command(message : types.Message):
	await message.answer('ssilkachalar', reply_markup=urlkb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_+1'),\
	                                        InlineKeyboardButton(text='DisLike', callback_data='like_-1'))

@dp.message_handler(commands=['test'])
async def test_commands(message : types.Message):
	await message.answer('video uchun botga ovoz ber', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback : types.Callback_Query):
	res = int(callback.data.split('_')[1])
	if f'{callback.from_user.id}' not in answ:
		answ[f'{callback.from_user.id}'] = res
		await callback.answer('siz ovoz berdingiz')
	else:
		await callback.answer('siz ovoz berb bolgansiz',show_alert=True)

	
executor.start_polling(dp, skip_updates=True)