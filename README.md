# CRUD-tutorial

## Run command

```
python -m main
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
```

