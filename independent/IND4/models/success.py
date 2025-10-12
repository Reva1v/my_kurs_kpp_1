from abc import ABC, abstractmethod

class Success(ABC):
    def __init__(self, subjects, scores):
        self.subjects = subjects
        self.scores = scores

    @abstractmethod
    def average_score(self):
        pass
