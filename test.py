import sqlite3
import random

conn = sqlite3.connect('D:/VS Code/sqlite dbs/test.db')
cursor = conn.cursor()

gms = []


def table_creation():
    cursor.execute('''CREATE TABLE games(
        ID INT,
        name TEXT,
        genre TEXT,
        year INT,
        studio TEXT
        )
        ''')


def game_create(id, n, g, yr, st):
    cursor.execute('''INSERT INTO games(ID, name, genre, year, studio)
    VALUES(id, n, g, yr, st)
    ''')

# game_create(1, 'Need for Speed: Undergroung 2',
#            'Гонки, Экшн, Нелинейность', 2004, 'Electronic Arts')
# game_create(2, 'Grand Theft Auto V',
#            'Экшн, Приключения, Нелинейность, Шутер', 2013, 'Rockstar Games')
# game_create(3, 'Borderlands 2', 'Шутер, RPG, Экшн',
#            '2012', 'Gearbox Software')
#game_create(4, 'Metro 2033 Redux', 'Шутер, Квест', 2014, '4A Games')
#game_create(5, 'Genshin Impact', 'RPG, Экшн, Квест', 2020, 'MiHoYo')
#game_create(6, 'Osu!', 'Музыкальная игра, Экшн', 2007, 'ppy')


vrnt = random.randint(0, 6)

cursor.execute('''SELECT name FROM games WHERE id=(?)''', [vrnt])
game = cursor.fetchall()

conn.commit()
print(game)


#cursor.execute('''SELECT * FROM students WHERE avg_score>9''')
'''
data = cursor.fetchall()
conn.commit()
print(data)'''
