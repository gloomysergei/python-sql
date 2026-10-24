import psycopg
from psycopg.rows import namedtuple_row, dict_row

with psycopg.connect(dbname = 'hexlet', user = 'sergey') as conn:
    
    with conn.cursor() as cur:
        cur.execute("TRUNCATE TABLE users RESTART IDENTITY")
        conn.commit
        
    new_users = [
    ("Bob", "1234562"),
    ("Alice", "293847"),
    ("John", "1010928"),
]
    with conn.cursor() as cur:
        cur.executemany("INSERT INTO users (username, phone) VALUES (%s, %s)", new_users)
        conn.commit()
    
    with conn.cursor(row_factory=namedtuple_row) as cur:
        cur.execute("SELECT * FROM users")
        for row in cur:
            print(row)
            
    with conn.cursor(row_factory = namedtuple_row) as cur:
        cur.execute("SELECT MAX(id) FROM users")
        id = cur.fetchone()
        print(id)
    