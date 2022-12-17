import sqlite3
# БД
db =sqlite3.connect("test1.sqlite") #создние бд проверяет есть ли она на пуути или нет

#создание запроса
#создание таблицы
c = db.cursor() #бязательно
c.execute("""CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY, 
name TEXT NOT NULL, 
email TEXT NOT NULL UNIQUE)
""")
#добовления данных
# c.execute("INSERT INTO users (name, email) VALUES ('Ивынов', 'warcraft@gmail.com')")
#c.execute("INSERT INTO users (name, email) VALUES ('Дмитрий', 'bibi@gmail.com')")
#c.execute("INSERT INTO users (name, email) VALUES ('роман', 'hibo@gmail.com')")
#c.execute("INSERT INTO users (name, email) VALUES ('Барис', 'bode@gmail.com')")

# c.executescript("""
# INSERT INTO users (name, email) VALUES ('Лена', 'Lengor@gmail.com');
# INSERT INTO users (name, email) VALUES ('Анастасия', 'hipora@gmail.com')
# """)
#вставка данных (последовательности )
# users = [
#     ("User 1", "dfde@gmail.com"),
#     ("User 2", "defd@gmail.com"),
#     ("User 2", "dfed@gmail.com"),
# ]
# c.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
#получения данных из таблицы
#db.commit()
email = "bibi@gmail.com"
# c.execute(f"SELECT * FROM users WHERE email = '{email}'")
# res = c.fetchone()
# print(res) SQL инекция привет не льзя не БЕЗОПАСНО
c.execute("SELECT * FROM users WHERE email = :email OR name = :name ", {"email": email, "name": "User 1" }) # good нет инекции
res = c.fetchone()
print(res)
c.execute("SELECT * FROM users")
res = c.fetchall()
for i in res:
    print(i, end="\n")

db.close() # закрытия`