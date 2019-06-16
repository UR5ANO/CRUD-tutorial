import psycopg2

from config.db import db_conf
from db_utils import select, insert, update, delete


def main():
	conn = None
	try:
		conn = psycopg2.connect(**db_conf)
		while True:
			s = input("Enter command:")
			if s == "exit":
				return
			elif s.startswith("select"):
				print(select(conn))
			elif s.startswith("insert"):
				_, name, password = s.split()
				print(insert(conn, name, password))
			elif s.startswith("update"):
				_, id, name, password = s.split()
				print(update(conn, id, name, password))
			elif s.startswith("delete"):
				_, id = s.split()
				print(delete(conn, id))
			else:
				print("Command should be one of:")
				print("select")
				print("insert <name> <password>")
				print("update <id> <field_name> <field_value>")
				print("delete <id>")
				print("exit")
	finally:
		conn.close()


if __name__ == "__main__":
	main()
