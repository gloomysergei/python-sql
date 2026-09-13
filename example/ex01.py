import psycopg

try:
    # Создаем соединение с базой hexlet
    conn = psycopg.connect("postgresql://sergey@/hexlet?host=/var/run/postgresql")
    print("Подключение работает")
except:
    print(f"Не удается установить подключение к базе данных")

sql = "CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255), phone VARCHAR(255));"
# Запрос выполняется через создание объекта курсора
cursor = conn.cursor()
cursor.execute(sql) # oтправляет SQL-строку на выполнение в БД.
conn.commit() # коммитим, т.е. сохраняем измемнения в БД
cursor.close() # закрывает курсор и освобождает ресурсы.

sql2 = "INSERT INTO users (username, phone) VALUES ('sergey', '123456789');"
cursor = conn.cursor()
cursor.execute(sql2)
conn.commit()
cursor.close()

sql3 = "SELECT * FROM users;"
cursor = conn.cursor()
cursor.execute(sql3)
for row in cursor:
    print(row)
cursor.close()
conn.close()

