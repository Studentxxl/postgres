import psycopg2

# Создание базы данных
conn = psycopg2.connect(dbname='postgres', user='postgres', password='RTy567', host='localhost')
cursor = conn.cursor()
conn.autocommit = True
# команда для создания базы данных metanit
sql = "CREATE DATABASE test"
# выполняем код sql
cursor.execute(sql)
print("База данных успешно создана")
cursor.close()
conn.close()