from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#admin uchun klaviatura
b1 = KeyboardButton('/Yuklash')
b2 = KeyboardButton('/bekor')
b3 = KeyboardButton("/Ortga")

button_admin = ReplyKeyboardMarkup(resize_keyboard=True)
button_back_admin = ReplyKeyboardMarkup(resize_keyboard=True)

button_admin.add(b1).add(b3)
button_back_admin.add(b2)