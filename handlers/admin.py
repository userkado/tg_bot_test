from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb, kb_client

ID = None

class FSMAdmin(StatesGroup):
	document = State()
	name = State()
	Author = State()



#moderatorni ID sini olib tekshiramiz
#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
	global ID
	ID=message.from_user.id
	await bot.send_message(message.from_user.id, 'boshliq amringizga muntazirmiz', reply_markup=admin_kb.button_admin)
	await message.delete()


#kitob yuklash jarayonini boshlash uchun dialog
#@dp.message_handler(commands="Yuklash", state=None)
async def com_start(message : types.Message):
	if message.from_user.id == ID:
		await FSMAdmin.document.set()
		await message.reply('kitobni yuklang', reply_markup=admin_kb.button_back_admin)



#@dp.message_handler(commands="Ortga")
async def  com_back(message : types.Message):
	await message.reply("Ok", reply_markup=kb_client)
	await message.delete()

#xolatdan chiqish 
#@dp.message_handler(state="*", commands='bekor')
#@dp.message_handler(Text(equals='bekor',ignore_case=True),state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		current_state =await state.get_state()
		if current_state is None:
			return
		await state.finish()
		await message.reply('OK', reply_markup=admin_kb.button_admin)


#1 chi javobli ushlash
#@dp.message_handler(content_types = ['file'],state=FSMAdmin.photo)
async def send_document(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['document'] = message.document.file_id
		await FSMAdmin.next()
		await message.reply('endi kitob nomini kiriting')

#2 chi javobli ushlash
#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state:FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['name'] = message.text
		await FSMAdmin.next()
		await message.reply('Mualifni kiriting')

#3 chi javobli ushlash

#oxirgi javobni ushlab undan foydalanishga o'tamiz
#@dp.message_handler(state=FSMAdmin.price)
async def load_author(message: types.Message, state: FSMContext):
	if message.from_user.id == ID:
		async with state.proxy() as data:
			data['Author'] = message.text
		await sqlite_db.sql_add_command(state)
		await message.reply('Yangi malumot saqlandi raxmat!!!', reply_markup=admin_kb.button_admin )
		await state.finish()



#xendlerlarni regisratsiyasi 
def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(com_start, commands="Yuklash", state=None)
	dp.register_message_handler(com_back, commands=["Ortga"] )
	dp.register_message_handler(cancel_handler, state="*", commands='bekor')
	dp.register_message_handler(cancel_handler, Text(equals='bekor',ignore_case=True),state="*")
	dp.register_message_handler(send_document, content_types = ['document'],state=FSMAdmin.document)
	dp.register_message_handler(load_name, state=FSMAdmin.name)
	dp.register_message_handler(load_author, state=FSMAdmin.Author)
	dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
