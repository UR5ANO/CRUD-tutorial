import unittest

from config.db import test_db_conf
from main.db_utils import db_connect, select, insert, update, delete


class SelectTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = db_connect(test_db_conf)
        cur = self.conn.cursor()
        cur.execute("insert into users(name, password) values ('roma', '111'), ('vova', '777')")
        cur.close()

    def tearDown(self):
        cur = self.conn.cursor()
        cur.execute("delete from users")
        cur.close()

    def test_select(self):
        rows = select(self.conn)
        assert len(rows) == 2
        roma = list(filter(lambda r: r[1] == "roma", rows))[0]
        assert roma[2] == "111"
        vova = list(filter(lambda r: r[1] == "vova", rows))[0]
        assert vova[2] == "777"


class InsertOneRowTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = db_connect(test_db_conf)

    def tearDown(self):
        cur = self.conn.cursor()
        cur.execute("delete from users")
        cur.close()

    def test_insert(self):
        roma_id = insert(self.conn, "roma", "111")
        rows = select(self.conn)
        assert len(rows) == 1
        roma = rows[0]
        assert roma[0] == roma_id
        assert roma[1] == "roma"
        assert roma[2] == "111"


class InsertMultipleRowsTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = db_connect(test_db_conf)

    def tearDown(self):
        cur = self.conn.cursor()
        cur.execute("delete from users")
        cur.close()

    def test_insert(self):
        roma_id = insert(self.conn, "roma", "111")
        vova_id = insert(self.conn, "vova", "777")
        rows = select(self.conn)
        assert len(rows) == 2
        roma = list(filter(lambda r: r[1] == "roma", rows))[0]
        assert roma[0] == roma_id
        assert roma[2] == "111"
        vova = list(filter(lambda r: r[1] == "vova", rows))[0]
        assert vova[0] == vova_id
        assert vova[2] == "777"


class UpdateNonExistingUserTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = db_connect(test_db_conf)

    def tearDown(self):
        cur = self.conn.cursor()
        cur.execute("delete from users")
        cur.close()

    def test_update(self):
        update_result = update(self.conn, 1, "name", "roma")
        assert update_result is False
        rows = select(self.conn)
        assert len(rows) == 0


class UpdateExistingUserTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = db_connect(test_db_conf)

        cur = self.conn.cursor()
        cur.execute("insert into users(name, password) values ('roma', '111') returning id")
        self.inserted_id = cur.fetchone()[0]
        cur.close()

    def tearDown(self):
        cur = self.conn.cursor()
        cur.execute("delete from users")
        cur.close()

    def test_update(self):
        update_result = update(self.conn, self.inserted_id, "name", "vova")
        assert update_result is True
        rows = select(self.conn)
        assert len(rows) == 1
        vova = rows[0]
        assert vova[0] == self.inserted_id
        assert vova[1] == "vova"
        assert vova[2] == "111"


class DeleteNonExistingUserTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = db_connect(test_db_conf)

    def tearDown(self):
        cur = self.conn.cursor()
        cur.execute("delete from users")
        cur.close()

    def test_delete(self):
        update_result = delete(self.conn, 1)
        assert update_result is False


class DeleteExistingUserTestCase(unittest.TestCase):

    def setUp(self):
        self.conn = db_connect(test_db_conf)

        cur = self.conn.cursor()
        cur.execute("insert into users(name, password) values ('roma', '111') returning id")
        self.inserted_id = cur.fetchone()[0]
        cur.close()

    def tearDown(self):
        cur = self.conn.cursor()
        cur.execute("delete from users")
        cur.close()

    def test_delete(self):
        update_result = delete(self.conn, self.inserted_id)
        assert update_result is True
        rows = select(self.conn)
        assert len(rows) == 0
