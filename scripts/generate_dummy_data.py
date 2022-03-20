import random

import psycopg2
from faker import Faker


def connect():
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute("SELECT version()")

        db_version = cur.fetchone()
        print(db_version)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Closed connection!!")


if __name__ == "__main__":
    connect()
    for i in range(20):
        print(random.randint(0, 9), random.randint(10, 100))
