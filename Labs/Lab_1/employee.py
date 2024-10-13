from bonus_calculator import StandardBonusCalculator, PerformanceBonusCalculator

class Employee:
    def __init__(self, name: str, position: str, salary: float, performance_score: float = 0):
        self.name = name
        self.position = position
        self.salary = salary
        self.performance_score = performance_score

    def get_standard_bonus(self):
        bonus_calculator = StandardBonusCalculator()
        return bonus_calculator.calculate_bonus(self.salary)

    def get_performance_bonus(self):
        bonus_calculator = PerformanceBonusCalculator()
        return bonus_calculator.calculate_bonus(self.salary, self.performance_score)
