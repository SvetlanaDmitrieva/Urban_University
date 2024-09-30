# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователя.


import sqlite3

connection = sqlite3.connect('not_telegram_2.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER ,
balance INTEGER NOT NULL
)
''')
for i in range (10):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i+1}', f'example{i+1}@gmail.com', ((i+1)*10), 1000))

for i in range(1, 10, 2):
    cursor.execute('UPDATE Users  SET balance = ? WHERE id = ?', (500, i))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

# cursor.execute('SELECT * FROM Users WHERE age != ?', (60,))
# results = cursor.fetchall()
# for res in results:
#     print(f"Имя: {res[1]} | Почта: {res[2]} | Возраст: {res[3]}  | Баланс: {res[3]}")

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
