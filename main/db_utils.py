import psycopg2

from typing import List


def select(
	conn: psycopg2.extensions.connection,
) -> List[tuple]:
	"""
	Этот метод достает все записи из таблицы `users`

	Параметры:
		conn - соединение (connection) с БД
	Возвращаемое значение:
		список строк таблицы, где строка представлена в виде кортежа
		(<id>, <name>, <password>) 
	"""
	cur = None
	try:
		cur = conn.cursor()
		cur.execute("select * from users order by name")
		return cur.fetchall()
	finally:
		cur.close()


def insert(
	conn: psycopg2.extensions.connection,
	name: str,
	password: str,
) -> int:
	"""
	Этот метод добавляет одну запись в таблицу `users`
	с заданными значениямо полей `name` и `password`

	Параметры:
		conn - соединение (connection) с БД
		name - значение поля name вставляемой строки
		password - значение поля password вставляемой строки
	Возвращаемое значение:
		одно число - id добавленного пользователя 
	"""
	raise NotImplementedError()


def update(
	conn: psycopg2.extensions.connection,
	id: int,
	field_name: str,
	field_value: str,
) -> bool:
	"""
	Этот метод модифицирует значение поля `field_name`
	на значение `field_value` в одной записи таблицы `users`
	по указанному `id`

	Параметры:
		conn - соединение (connection) с БД
		id - id пользователя, запись о котором нужно модифицировать
		field_name - название поля, которое нужно модифицировать
		field_value - значение поля, которое нужно модифицировать
	Возвращаемое значение:
		True, если пользователь с таким `id` существует,
		иначе False 
	"""
	raise NotImplementedError()


def delete(
	conn: psycopg2.extensions.connection,
	id: int,
) -> bool:
	"""
	Этот метод удаляет одну запись таблицы `users`
	по указанному `id`

	Параметры:
		conn - соединение (connection) с БД
		id - id пользователя, запись о котором нужно удалить
	Возвращаемое значение:
		True, если пользователь с таким `id` существует и был удален,
		иначе False 
	"""
	cur = None
	try:
		cur = conn.cursor()
		cur.execute("delete from users where id = {}".format(id))
		return cur.rowcount > 0
	finally:
		cur.close()
