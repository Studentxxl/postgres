import psycopg2

# Добавление данных
conn = psycopg2.connect(dbname="test", user="postgres", password="RTy567", host="127.0.0.1")
cursor = conn.cursor()
# добавляем строку в таблицу people
cursor.execute("INSERT INTO people (login, pass) VALUES "
               "('delin', 'gt567'), "
               "('jim', '3ui'), "
               "('dgty', 'dfrfrt56'), "
               "('locdrtyk', 'dfgff123'), "
               "('firex', '12w245'), "
               "('optup', 'dddgtyfg45') ")
# выполняем транзакцию
conn.commit()
print("Данные добавлены")
cursor.close()
conn.close()