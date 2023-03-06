from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, search, Inline_kb
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state  import State, StatesGroup
from handlers import pagination

class FSMClient_Author(StatesGroup):
	search_author =State()

class FSMClient_Name(StatesGroup):
	search_name =State()


# @dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id,"Salom o'zingizga kerakli kitobni topish uchun SEARCH tugmasini bosing", reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Bot bn gaplashish uchun u bn birga shaxsiy chatga oting : \n//t.me/ARMfarduBot')

# @dp.message_handler(commands=['ish_garfigi'])
async def arm_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Duyshanba - Juma 08:00 dan 18:00 gachor Shanba 08:00 dan 15:00 gachor ')

# @dp.message_handler(commands=['Joylashuvi'])
async def arm_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Murabbiylar kochasi 1 uy FDU ')


#@dp.message_handler(commands=["Search"])
async def arm_royxat_command(message : types.Message):
	await message.reply("Kitob nomi boyicha qidirish uchun NAME tugmasidan foydalaning\nKitob mualifi boyicha qidirish uchun AUTHOR tugmasidan foydalaning", reply_markup=search)

@dp.message_handler(commands='Author', state=None)
async def commands_search_author(message : types.Message):
	await FSMClient_Author.search_author.set()
	await message.reply("Kitob mualifini kiriting")
	await message.delete()

@dp.message_handler(state=FSMClient_Author.search_author)
async def send_search_author(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['search'] = message.text
	search = await sqlite_db.sql_search_author(state)
	for ret in search:
		await bot.send_document(message.from_user.id, ret[1], f'\nID: {ret[0]},\nNomi:{ret[2]},\nMualifi: {ret[-1]}')
	await state.finish()

@dp.message_handler(commands='Name', state=None)
async def commands_search_author(message : types.Message):
	await FSMClient_Name.search_name.set()
	await message.reply("Kitob nomini kiriting")
	await message.delete()

@dp.message_handler(state=FSMClient_Name.search_name)
async def send_search_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['search'] = message.text
	search = await sqlite_db.sql_search_name(state)
	listlar=[(3, 'BQACAgIAAxkBAAIGrGPPuHJnzxLEJQABU8cKl2ESx45UDgAC8SEAAinCeErSWWwhlpkRJi0E', 'Религиовведение учебник', 'Гений'), (4, 'BQACAgIAAxkBAAIGtmPPuXQmhsWeFlHMmZOmbhnMHy0iAAL2IQACKcJ4Si3QjpU3qU0fLQQ', 'Религиовведение учебник', 'Гений'),(3, 'BQACAgIAAxkBAAIGrGPPuHJnzxLEJQABU8cKl2ESx45UDgAC8SEAAinCeErSWWwhlpkRJi0E', 'Религиовведение учебник', 'Гений'), (4, 'BQACAgIAAxkBAAIGtmPPuXQmhsWeFlHMmZOmbhnMHy0iAAL2IQACKcJ4Si3QjpU3qU0fLQQ', 'Религиовведение учебник', 'Гений'),(3, 'BQACAgIAAxkBAAIGrGPPuHJnzxLEJQABU8cKl2ESx45UDgAC8SEAAinCeErSWWwhlpkRJi0E', 'Религиовведение учебник', 'Гений'), (4, 'BQACAgIAAxkBAAIGtmPPuXQmhsWeFlHMmZOmbhnMHy0iAAL2IQACKcJ4Si3QjpU3qU0fLQQ', 'Религиовведение учебник', 'Гений'),(3, 'BQACAgIAAxkBAAIGrGPPuHJnzxLEJQABU8cKl2ESx45UDgAC8SEAAinCeErSWWwhlpkRJi0E', 'Религиовведение учебник', 'Гений'), (4, 'BQACAgIAAxkBAAIGtmPPuXQmhsWeFlHMmZOmbhnMHy0iAAL2IQACKcJ4Si3QjpU3qU0fLQQ', 'Религиовведение учебник', 'Гений'),(3, 'BQACAgIAAxkBAAIGrGPPuHJnzxLEJQABU8cKl2ESx45UDgAC8SEAAinCeErSWWwhlpkRJi0E', 'Религиовведение учебник', 'Гений'), (4, 'BQACAgIAAxkBAAIGtmPPuXQmhsWeFlHMmZOmbhnMHy0iAAL2IQACKcJ4Si3QjpU3qU0fLQQ', 'Религиовведение учебник', 'Гений'),(3, 'BQACAgIAAxkBAAIGrGPPuHJnzxLEJQABU8cKl2ESx45UDgAC8SEAAinCeErSWWwhlpkRJi0E', 'Религиовведение учебник', 'Гений'), (4, 'BQACAgIAAxkBAAIGtmPPuXQmhsWeFlHMmZOmbhnMHy0iAAL2IQACKcJ4Si3QjpU3qU0fLQQ', 'Религиовведение учебник', 'Гений')]
	print(type(listlar))
	len_items = len(listlar)
	
	print(len_items)
	pagin = await pagination.Pagination(listlar)
    # if len_items < 10 :
    # 	msg = await pagination.collect_data(0, len_items)
    #     markup = Inline_kb.items_keyboard(search, 0, len_items)
    # else:
    #     msg = await pagination.collect_data(0, 10)
    # await message.answer(msg, reply_markup=markup, parse_mode="HTML")


	
	#for ret in search:
	#	await bot.send_document(message.from_user.id, ret[1], f"\nID: {ret[0]},\nNomi:{ret[2]},\nMualifi: {ret[-1]}", reply_markup=kb_client)
	await state.finish()










def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start', 'help'])
	dp.register_message_handler(arm_open_command, commands=['ish_garfigi'])
	dp.register_message_handler(arm_place_command, commands=['Joylashuvi'])
	dp.register_message_handler(arm_royxat_command, commands=['Search'])