import psycopg2 as pg
import os
from dotenv import load_dotenv
from typing import Any

load_dotenv()

DB_CONFIG: dict[str, Any] = {
    "host": os.getenv("DB_HOST"),
    "dbname": os.getenv("DB_NAME"),  # type: ignore
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

print(DB_CONFIG)


def executeInput():
    """Executes a list of queries and returns the results of the LAST query (if any)."""
    rows = []
    con = pg.connect(**DB_CONFIG)
    cur = con.cursor()

    try:
        cur.execute(open("input.sql").read())
        con.commit()

        if cur.description:
            rows = cur.fetchall()
    except pg.Error as e:
        print(f"Error: {e}")
        con.rollback()
    finally:
        cur.close()
        con.close()

    return rows


def execute(query: str):
    """Executes a single query and returns the results."""
    rows = None
    con = pg.connect(**DB_CONFIG)
    cur = con.cursor()

    try:
        cur.execute(query)
        con.commit()

        if cur.description:
            rows = cur.fetchall()

    except pg.Error as e:
        print(f"Error: {e}")
        con.rollback()
    finally:
        cur.close()
        con.close()

    return rows


def dropTable(tableName: str):
    """Drops a table."""
    execute(f"drop table {tableName}")
