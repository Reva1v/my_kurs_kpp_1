import sqlite3

class Database:
    def __init__(self, db_name="students.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            group_number TEXT NOT NULL,
            birth_date TEXT,
            address TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS success (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            score REAL NOT NULL,
            is_desired INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
        """)

        self.connection.commit()

    def close(self):
        self.connection.close()
