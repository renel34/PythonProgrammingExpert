class Employee:
    average_age = 0
    average_salary = 0
    nbr_employee = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.nbr_employee += 1
        Employee.average_age += self.age
        Employee.average_salary += self.salary

empl1 = Employee("Rene", 60, 58000)
empl2 = Employee("Luc", 58, 40000)
print(Employee.average_age)