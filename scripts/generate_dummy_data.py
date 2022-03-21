import random
import time

import psycopg2


def transact(query):
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")
        cur = conn.cursor()

        cur.execute(query)

        product_info = cur.fetchone()
        print(product_info)

        conn.commit()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("Closed connection!!")


def insert_products(products):

    for product_id, amount in products.items():
        sql_insert = f"""
            INSERT INTO inventory.products(id, amount)
            VALUE ('{product_id}', '{amount}');
        """
        transact(sql_insert)


def update_product(product_id, amount):

    sql_update = f"""
           UPDATE inventory.products(id, amount)
           SET amount = {amount}
           WHERE id = '{product_id}';
       """
    transact(sql_update)


if __name__ == "__main__":
    products_dict = {
        'pen': 10,
        'pencil': 5,
        'eraser': 6,
        'book': 9,
        'sharpener': 15
    }
    insert_products(products_dict)

    while True:
        time.sleep(5)
        update_product(random.choice(list(products_dict)), random.randint(0, 50))
