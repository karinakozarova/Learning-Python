import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

class Team:
    def __init__(self,company,employees):
        self.company = company
        self.employees = employees

    def print_employees(self):
        print("Employees at {}:".format(self.company),end=" ")
        for employee in self.employees:
            print(employee.name,end=" ")
        print()

    def total_salaries(self):
        salaries = 0.0
        for employee in self.employees:
            salaries += employee.pay
        return salaries

    def hire_employee(self,employee):
        self.employees.append(employee)

    def fire_employee(self,employee):
        try:
            self.employees.remove(employee)
        except ValueError:
            logging.warning("tried to fire employee that was not hired")

class Employee:
    
    raise_amount = 1.1
    start_amount = 40000
    def __init__(self,company,name,pay):
        self.company = company
        self.name = name
        self.pay = int(pay)
        self.mail = self.employee_mail()

    def employee_mail(self):
        return "{}@{}.com".format(self.name.lower(),self.company.lower())

    def apply_raise(self):
        self.pay = int(self.pay*Employee.raise_amount)

class Intern(Employee):
    intern_payment = 0
    def __init__(self,company,name):
        super().__init__(company,name,Intern.intern_payment)

    def apply_raise(self):
        if self.pay == Intern.intern_payment:
            self.pay = Employee.start_amount
        else:
            Employee.apply_raise(self)

    
emp1 = Employee("Google","Bryan",90000)
intern1 = Intern("Google","Ivan")

employees = []
employees.append(emp1)
employees.append(intern1)

team = Team("Google",employees)
team.hire_employee(emp1)
print(team.total_salaries())

team.fire_employee(Employee("Google","Bryan",90000))

team.print_employees()
print(team.total_salaries())

# print(emp1.employee_mail())
# print(emp1.name)
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# print(intern1.employee_mail())
# print(intern1.name)
# print(intern1.pay)
# intern1.apply_raise()
# intern1.apply_raise()
# print(intern1.pay)

