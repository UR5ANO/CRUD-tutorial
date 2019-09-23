from config.db import db_conf
from main.db_utils import db_connect, select, insert, update, delete


def main():
    conn = None
    try:
        conn = db_connect(db_conf)
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
                _, id, field_name, field_value = s.split()
                print(update(conn, id, field_name, field_value))
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
