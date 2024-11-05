class Employee:
    def __init__(self, base_salary, overtime, rate):
        self.base_salary = base_salary
        self.overtime = overtime
        self.rate = rate
    
    def get_wage(self):
        return self.base_salary + (self.overtime * self.rate)
    
john = Employee(10000, 40, 50)
witney = Employee(10000, 5, 40)
print(f"Witney's Salary is {witney.get_wage()}")
print(f"John's Salary is {john.get_wage()}")