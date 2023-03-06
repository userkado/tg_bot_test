import sqlite3 as sq 
from create_bot import bot


def sql_start():
	global base, cur
	base = sq.connect('FARDU_ARM_KITOB.db')
	cur = base.cursor()
	if base:
		print('Data base connected OK!')
	base.execute('CREATE TABLE IF NOT EXISTS kitoblar(book_id integer PRIMARY KEY, kitob_pdf TEXT, name TEXT, Author TEXT) ')
	base.commit()



async def sql_add_command(state):
	async with state.proxy() as data:
		cur.execute('INSERT INTO kitoblar (kitob_pdf, name, Author) VALUES (?, ?, ?)', tuple(data.values()))
		base.commit()

async def sql_search_author(state):
	async with state.proxy() as data:
		search = data['search']
		return cur.execute("SELECT * FROM kitoblar WHERE Author LIKE ?", ("%"+search+"%",)).fetchall()

async def sql_search_name(state):
	async with state.proxy() as data:
		search = data['search']
		return cur.execute("SELECT * FROM kitoblar WHERE name LIKE ?", ("%"+search+"%",)).fetchall()

