class Employee:
    def __init__(self, name, salary, days_worked, bonus_percent=0):
        self._name = name
        self._salary = salary
        self._days_worked = days_worked
        self._bonus_percent = bonus_percent

    def calculate_salary(self):
        return (self._salary / 30) * self._days_worked

    def calculate_bonus(self):
        base_salary = self.calculate_salary()
        bonus = (base_salary / 100) * self._bonus_percent
        return bonus

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary

    def get_days_worked(self):
        return self._days_worked

    def set_days_worked(self, days):
        self._days_worked = days

    def get_bonus_percent(self):
        return self._bonus_percent

    def set_bonus_percent(self, percent):
        self._bonus_percent = percent


class Manager(Employee):
    bonus_amount = 100

    def __init__(self, name, salary, days_worked, subordinates_count, bonus_percent=0):
        super().__init__(name, salary, days_worked, bonus_percent)
        self._subordinates_count = subordinates_count

    def report(self):
        return f"Manager {self._name} manages {self._subordinates_count} employees."

    def calculate_bonus(self):
        base_bonus = super().calculate_bonus()
        bonus = base_bonus + (self._subordinates_count * Manager.bonus_amount)
        return bonus

    def get_subordinates_count(self):
        return self._subordinates_count

    def set_subordinates_count(self, count):
        self._subordinates_count = count


if __name__ == "__main__":
    employee1 = Employee("Ivan", 15000, 25, 5)
    employee2 = Employee("Olena", 18000, 20)
    manager1 = Manager("Petro", 25000, 28, subordinates_count=10, bonus_percent=10)
    manager2 = Manager("Svitlana", 28000, 22, subordinates_count=5, bonus_percent=7)

    employees_list = [employee1, employee2, manager1, manager2]

    for person in employees_list:
        print(f"{person.get_name()}: salary = {person.calculate_salary():.2f}, bonus = {person.calculate_bonus():.2f}")
        if isinstance(person, Manager):
            print(person.report())
