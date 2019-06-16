import psycopg2

from config.db import db_conf

conn = psycopg2.connect(**db_conf)
cur = conn.cursor()
cur.execute("select * from users order by password desc, name desc")
print(cur.fetchall())
cur.close()
conn.close()
