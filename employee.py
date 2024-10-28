class Employee:

    employee_number = 0

    def __init__(self, first_name, last_name):
        Employee.employee_number = Employee.employee_number + 1
        self.employee_number = Employee.employee_number
        self.first_name = first_name
        self.last_name = last_name

    def print_information(self):
        print(f"Employee {self.first_name} {self.last_name} - # {self.employee_number}")

class HourlyPaid(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.hourly_salary = salary
        self.has_free_coffee = False

    def print_information(self):
        super().print_information()
        print(f" - Salary: {self.hourly_salary} per hour")

    def can_use_employee_lounge(self):
        return False

class MonthlyPaid(Employee):
    def __init__(self, first_name, last_name, salary, benefits):
        super().__init__(first_name, last_name)
        self.monthly_salary = salary
        self.benefits = benefits
        self.has_free_coffee = True

    def print_information(self):
        super().print_information()
        print(f" - Monthly: {self.monthly_salary} per month")
        print(f" - Benefits: {self.benefits}")

    def use_benefits(self):
        print(f"{self.name} uses benefit {self.benefits}")

employee1 = Employee("Juha", "Tauriainen")
employee2 = HourlyPaid("John", "Von Tauren", 12)
employee3 = MonthlyPaid("Peter", "Pan", 2000, "dental")
employee4 = MonthlyPaid("Anna", "Kornikova", employee2.hourly_salary * 80, "healthcare")

for employee in [employee1, employee2, employee3, employee4]:
    employee.print_information()