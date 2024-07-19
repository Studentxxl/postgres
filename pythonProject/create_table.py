import psycopg2

# Создание таблицы
conn = psycopg2.connect(dbname="test", user="postgres", password="RTy567", host="127.0.0.1")
cursor = conn.cursor()
# создаем таблицу people
cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, login VARCHAR(16), pass VARCHAR(16))")
# поддверждаем транзакцию
conn.commit()
print("Таблица people успешно создана")
cursor.close()
conn.close()