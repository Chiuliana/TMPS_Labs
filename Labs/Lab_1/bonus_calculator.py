class BonusCalculator:
    def calculate_bonus(self, salary: float):
        raise NotImplementedError("This method should be overridden")

class StandardBonusCalculator(BonusCalculator):
    def calculate_bonus(self, salary: float):
        return salary * 0.1

class PerformanceBonusCalculator(BonusCalculator):
    def calculate_bonus(self, salary: float, performance_score: float):
        return salary * 0.1 + salary * 0.05 * performance_score
