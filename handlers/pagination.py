from typing import List
from aiogram import types

from keyboards import Inline_kb





class Pagination:
    def init(self, items: List):
        self.__items = items



    async def collect_data(self, start: int, end: int)->str:
        i = 1
        text = ""
        for item in self.__items[start:end]:
            text += f"<b>{i})</b> {item[1]} - {item[2]}\n"
            i += 1
        return text

    async def select_item(self, item_id: int)->List:
        for llist in self.__items:
            if llist[0] == item_id:
                break
        return llist

    async def start_message(self, message: types.Message):
        len_items = len(self.__items)
        if len_items < 10:
            msg = await self.collect_data(0, len_items)
            markup = items_keyboard(self.__items, 0, len_items)
        else:
            msg = await self.collect_data(0, 10)
            markup = items_keyboard(self.__items, 0, 10)
        await message.answer(msg, reply_markup=markup, parse_mode="HTML")

    async def prev(self, start, end, max_pages, call: types.CallbackQuery):
        if start == 0 and start - 10 <= 0:
            await call.answer("Bu birinchi sahifa", cache_time=1)
        elif max_pages - end < 10 and max_pages - end >= 0:  # 27 20
            new_start = start - 10
            new_end = start
            msg = await self.collect_data(start=new_start, end=new_end)
            markup = items_keyboard(self.__items, start=new_start, end=new_end)
            await call.message.edit_text(msg, reply_markup=markup, parse_mode="HTML")
        else:
            msg = await self.collect_data(start=start - 10, end=end - 10)
            markup = items_keyboard(self.__items, start=start - 10, end=end - 10)
            await call.message.edit_text(msg, reply_markup=markup, parse_mode="HTML")

    async def next(self, call: types.CallbackQuery, start, end, max_pages):
        if max_pages - end < 10 and max_pages - end > 0:
            msg = await self.collect_data(start=end, end=max_pages)
            markup = items_keyboard(self.__items, start=end, end=max_pages)
            await call.message.edit_text(msg, reply_markup=markup, parse_mode="HTML")
        elif max_pages - end <= 0:
            await call.answer("Bu so'nggi sahifa", show_alert=True, cache_time=1)
        else:
            msg = await self.collect_data(start=start + 10, end=end + 10)
            markup = items_keyboard(self.__items, start=start + 10, end=end + 10)
            await call.message.edit_text(msg, reply_markup=markup, parse_mode="HTML")