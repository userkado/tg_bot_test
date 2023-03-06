from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Ish_garfigi')
b2 = KeyboardButton('/Joylashuvi')
b3 = KeyboardButton("/Search")
b4 = KeyboardButton("/Author")
b5 = KeyboardButton("/Name")

#b4 = KeyboardButton('/raqam bn ulashish!',request_contact=True)
#b5 = KeyboardButton('/Joylashuv lokatsiyasi bn ulashish!',request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
search =ReplyKeyboardMarkup(resize_keyboard=True)



kb_client.add(b3).row(b1,b2)#.row(b4,b5)
search.add(b4).add(b5)