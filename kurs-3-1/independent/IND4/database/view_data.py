import sqlite3

con = sqlite3.connect('../students.db')
cur = con.cursor()

print("Students:")
for row in cur.execute('SELECT * FROM students'):
    print(row)

print("\nSuccess records:")
for row in cur.execute('SELECT * FROM success'):
    print(row)

con.close()
