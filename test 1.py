import sqlite3

conn = sqlite3.connect('C:/Users/User/Desktop/test1.db')
cursor = conn.cursor()

def table_creation():
    cursor.execute('''CREATE TABLE games(
        ID INT,
        name TEXT,
        genre TEXT,
        year INT,
        studio TEXT
        )
        ''')


table_creation()


conn.commit()










#cursor.execute('''SELECT * FROM students WHERE avg_score>9''')
'''
data = cursor.fetchall()

conn.commit()

print(data)'''