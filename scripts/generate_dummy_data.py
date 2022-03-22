import psycopg2


def transact(query, action):
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="postgres")
        cur = conn.cursor()

        cur.execute(query)

        product_info = cur.fetchone()[0]
        print(f"{action} {product_info}")

        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


def insert_products(products):

    for product_id, quantity in products.items():
        sql_insert = f"""
            INSERT INTO inventory.products(product_id, quantity, created_at, updated_at)
            VALUES ('{product_id}', {quantity}, NOW()::timestamp, NOW()::timestamp)
            RETURNING product_id;
        """
        transact(sql_insert, "Created")


def update_product(product_id, quantity):

    sql_update = f"""
           UPDATE inventory.products
           SET quantity = {quantity}, updated_at = NOW()::timestamp
           WHERE product_id = '{product_id}'
           RETURNING product_id;
       """
    transact(sql_update, "Updated")


if __name__ == "__main__":
    import random
    import time

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
