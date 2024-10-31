from employee import Employee

if __name__ == "__main__":
    employee1 = Employee("John Doe", "Developer", 5000)
    print(f"Standard Bonus: {employee1.get_standard_bonus()}")

    employee2 = Employee("Jane Smith", "Manager", 8000, performance_score=4)
    print(f"Performance Bonus: {employee2.get_performance_bonus()}")
