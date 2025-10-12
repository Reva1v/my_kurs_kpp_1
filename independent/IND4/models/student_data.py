from independent.IND4.models.desired_success import DesiredSuccess
from independent.IND4.models.student import Student
from independent.IND4.models.success import Success


class StudentData:
    def __init__(self, student: Student, real_success: Success, desired_success: DesiredSuccess):
        self.student = student
        self.real_success = real_success
        self.desired_success = desired_success

    def calculate_average_real(self):
        if self.real_success.scores:
            return sum(self.real_success.scores) / len(self.real_success.scores)
        return 0.0

    def calculate_average_desired(self):
        return self.desired_success.average_score()
