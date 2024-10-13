from bonus_calculator import BonusCalculator

class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary
        self.bonus_calculator = BonusCalculator()

    def get_bonus(self):
        return self.bonus_calculator.calculate_bonus(self.salary)
