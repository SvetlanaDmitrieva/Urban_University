import sqlite3

connection = sqlite3.connect('not_telegram.db')
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

cursor.execute('SELECT * FROM Users WHERE age != ?', (60,))
results = cursor.fetchall()
for res in results:
    print(f"Имя: {res[1]} | Почта: {res[2]} | Возраст: {res[3]}  | Баланс: {res[3]}")

connection.commit()
connection.close()

