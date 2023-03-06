from typing import List

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

base_cd = CallbackData("items", "item", "start", "end", "max_pages")
pagination_cd = CallbackData("pagination", "start", "end", "max_pages", "action")


# create keyboards
def items_keyboard(items: List, start: int, end: int):
    markup = InlineKeyboardMarkup()
    page_size = end-start
    title = 0
    if page_size < 9 and page_size > 6: markup.row_width = 4
    elif page_size == 6 or page_size == 5: markup.row_width=3
    elif page_size <= 4 and page_size >= 2: markup.row_width = 2
    elif page_size == 1: markup.row_width = 1
    else: markup.row_width=5
    max_pages = len(items)
    items = items[start:end]
    i = 1
    for item in items:
        markup.insert(
            InlineKeyboardButton(
                text=str(i),
                callback_data=base_cd.new(item=item[0], start=start, end=end, max_pages=max_pages)
            )
        )
        if i == end-start: break
        else: i+=1


    # make bottom buttons
    bottom_buttons = [
        InlineKeyboardButton(
            text="⬅️",
            callback_data=pagination_cd.new(
                start=start, end=end, max_pages=max_pages, action="prev"
            )
        ),

        InlineKeyboardButton(
            text=f"{title+end//10 if end%10==0 else start//10+1}",
            callback_data=pagination_cd.new(
                start=start, end=end, max_pages=max_pages, action="none"
            )
        ),
        InlineKeyboardButton(
            text="➡️",
            callback_data=pagination_cd.new(
                start=start, end=end, max_pages=max_pages, action="next"
            )
        )
    ]

    # add bottom buttons
    markup.row()
    markup.row_width=3
    for bottom in bottom_buttons:
        markup.insert(bottom)

    return markup