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


def executeList(queries: list[str]):
    """Executes a list of queries and returns the results of the LAST query (if any)."""
    rows = []
    con = pg.connect(**DB_CONFIG)
    cur = con.cursor()

    try:
        for q in queries:
            try:
                cur.execute(q)
                con.commit()

                if cur.description:
                    rows = cur.fetchall()

            except pg.Error as e:
                print(f"Error running query: {q}\n{e}")
                con.rollback()

    except Exception as e:
        print(f"Connection error: {e}")
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
