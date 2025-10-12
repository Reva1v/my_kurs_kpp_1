from independent.IND4.models.success import Success

class DesiredSuccess(Success):
    def __init__(self, subjects, scores, desired_average):
        super().__init__(subjects, scores)
        self.desired_average = desired_average

    def average_score(self):
        return self.desired_average