class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_bonus(self):
        # simple bonus calculation based on salary
        return self.salary * 0.1
