import psycopg
from ex05 import get_order_sum
from psycopg.rows import namedtuple_row, dict_row

with psycopg.connect(dbname = 'hexlet', user = 'sergey') as conn:
    
    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE orders, customers RESTART IDENTITY")
        conn.commit()
    
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id SERIAL PRIMARY KEY,
                customer_name VARCHAR(100) NOT NULL
            );
        """)
        conn.commit()
        
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id SERIAL PRIMARY KEY,
                customer_id INTEGER REFERENCES customers(customer_id),
                order_date DATE NOT NULL,
                total_amount NUMERIC NOT NULL
            );
            """)
        
    name = [
        ('John Smith',),
        ('Emma Johnson',),
        ('Michael Brown',),
        ('Olivia Davis',),
        ('William Wilson',),
        ('Sophia Taylor',),
        ('James Anderson',),
        ('Isabella Thomas',),
        ('Robert Jackson',),
        ('Emily White',),
    ]
    
    order = [
        (1, '2023-05-15', 150),
        (2, '2023-05-20', 230),
        (3, '2023-06-05', 75),
        (4, '2023-06-12', 310),
        (5, '2023-06-28', 180),
        (1, '2023-07-10', 210),
        (6, '2023-07-22', 95),
        (7, '2023-08-05', 350),
        (8, '2023-08-18', 120),
        (9, '2023-09-01', 280),
        (10, '2023-09-15', 165),
        (2, '2023-09-30', 220),
        (2, '2023-10-12', 190),
        (4, '2023-10-25', 330),
        (5, '2023-11-08', 140),
        (4, '2023-11-20', 260),
        (4, '2023-12-02', 110),
        (8, '2023-12-15', 320),
        (8, '2023-12-28', 175),
        (10, '2024-01-10', 290),
        (1, '2024-01-22', 130),
        (1, '2024-02-05', 240),
        (3, '2024-02-18', 800),
        (3, '2024-03-01', 340),
        (3, '2024-03-15', 160),
        (3, '2024-03-28', 270),
        (3, '2024-04-10', 100),
        (7, '2024-04-23', 360),
        (7, '2024-05-05', 135),
        (10, '2024-05-18', 250)
    ]
    
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO customers (customer_name) VALUES (%s)", name)
        conn.commit()
    
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO orders (customer_id, order_date, total_amount) VALUES (%s, %s, %s)", order)    
        conn.commit()
       
   
    result = get_order_sum(conn, 5)
    print(result)
   
        
# выполнить запрос - общая сумма заказов каждого покупателя за конкретный месяц независимо от года
# например - январь: 01
"""
В отчёт входят покупатели, у которых есть хотя бы один заказ за указанный месяц. Функция только читает данные. 
Переданное соединение принадлежит вызывающему коду, который сам завершает транзакцию через commit() 
или rollback().

Допишите в файле src/solution.py функцию get_order_sum(), которая принимает соединение и месяц,
а возвращает общую сумму заказов каждого покупателя за этот месяц. 
Функция возвращает одну строку, где каждому покупателю отведена своя строка текста. 
Строки разделены символом \n и отсортированы по имени покупателя. 
Например, за январь функция вернёт такой текст.

Покупатель Emily White совершил покупок на сумму 290
Покупатель John Smith совершил покупок на сумму 130
"""
