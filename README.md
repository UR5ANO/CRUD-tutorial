# CRUD-tutorial

## Run command

```
python -m main.main
```

## Run tests

```
python -m unittest test.db_utils_test
```

## How to configure database?

1. Create `config/` directory.
2. Put `db.py` file to `config/` with the following content:

```
db_conf = {
    "host": <db host>,
    "database": <your db name>,
    "user": <your user>,
    "password": <your password>,
}

test_db_conf = {
    "host": <db host>,
    "database": <your db name>,
    "user": <your user>,
    "password": <your password>,
}
```

Where `db_conf` is application DB config and `test_db_conf` is test database.
Script for initializing database is located under `queries/create_users.sql`.
