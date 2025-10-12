from database.database import Database
from independent.IND4.models.desired_success import DesiredSuccess

from independent.IND4.models.student import Student
from independent.IND4.models.student_data import StudentData
from independent.IND4.models.success import Success
from services.student_service import StudentService

db = Database()

student = Student(full_name="John Doe", group_number="B01", birth_date="2000-01-01", address="123 Main St")
student2 = Student(full_name="Marcus", group_number="B02", birth_date="2000-03-06", address="20 Main St")

real_subjects = ["Math", "Physics", "English"]
real_scores = [85, 90, 88]

class RealSuccess(Success):
    def average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

real_success = RealSuccess(real_subjects, real_scores)

desired_subjects = ["Math", "Physics", "English"]
desired_scores = [90, 92, 90]
desired_average = 90.7

desired_success = DesiredSuccess(desired_subjects, desired_scores, desired_average)

student_data = StudentData(student, real_success, desired_success)

student_data2 = StudentData(student2, real_success, desired_success)

service = StudentService(db)
service.save_student_data(student_data)
service.save_student_data(student_data2)

print("Student data saved successfully.")

db.close()
