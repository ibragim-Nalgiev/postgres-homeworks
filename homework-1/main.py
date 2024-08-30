"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

import csv

customer = []
with open('north_data/customers_data.csv', 'r', encoding='utf-8') as file:
    file_reader_1 = csv.reader(file, delimiter=",")
    for i in file_reader_1:
        customer.append(tuple(i))

try:
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="0606") as conn:
        with conn.cursor() as cur:
            cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', customer[1:])
            cur.execute('SELECT * FROM customers')
            rows = cur.fetchall()
            for row in rows:
                print(row)

finally:
        conn.close()


order = []
with open('north_data/orders_data.csv', 'r', encoding='utf-8') as file:
    file_reader_2 = csv.reader(file, delimiter=",")
    for i in file_reader_2:
        order.append(tuple(i))

with psycopg2.connect(host="localhost", database="north", user="postgres", password="0606") as conn:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', order[1:])
        cur.execute('SELECT * FROM orders')
        rows = cur.fetchall()
        for row in rows:
            print(row)

conn.close()

employee = []
with open('north_data/employees_data.csv', 'r', encoding='utf-8') as file:
    file_reader_3 = csv.reader(file, delimiter=",")
    for i in file_reader_3:
        employee.append(tuple(i))

with psycopg2.connect(host="localhost", database="north", user="postgres", password="0606") as conn:
    with conn.cursor() as cur:
        cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s)', employee[1:])
        cur.execute('SELECT * FROM employees')
        rows = cur.fetchall()
        for row in rows:
            print(row)

conn.close()
