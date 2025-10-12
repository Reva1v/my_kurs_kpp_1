from independent.IND4.database.database import Database
from independent.IND4.models.student_data import StudentData

class StudentService:
    def __init__(self, db: Database):
        self.db = db

    def save_student_data(self, student_data: StudentData):
        cursor = self.db.connection.cursor()

        cursor.execute("""
            INSERT INTO students (full_name, group_number, birth_date, address)
            VALUES (?, ?, ?, ?)
        """, (
            student_data.student.get_full_name(),
            student_data.student.get_group_number(),
            student_data.student.get_birth_date(),
            student_data.student.get_address()
        ))
        student_id = cursor.lastrowid

        for subject, score in zip(student_data.real_success.subjects, student_data.real_success.scores):
            cursor.execute("""
                INSERT INTO success (student_id, subject, score, is_desired)
                VALUES (?, ?, ?, ?)
            """, (student_id, subject, score, 0))

        for subject, score in zip(student_data.desired_success.subjects, student_data.desired_success.scores):
            cursor.execute("""
                INSERT INTO success (student_id, subject, score, is_desired)
                VALUES (?, ?, ?, ?)
            """, (student_id, subject, score, 1))

        self.db.connection.commit()