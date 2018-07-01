import unittest

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

class TeamTest(unittest.TestCase):
    def setUp(self):  
        self.emp1 = Employee("Google","Bryan",90000)
        self.intern1 = Intern("Google","Ivan")

        self.employees = []

        self.employees.append(self.emp1)
        self.employees.append(self.intern1)

        self.team1 = Team("Google",self.employees)
        self.team2 = Team("Google",self.employees)
        self.team3 = Team("Google",[self.emp1])

    def test_create_same_objects(self):
        self.assertEqual(self.team1.company, self.team2.company)  
        self.assertEqual(self.team1.employees, self.team2.employees)  

    def test_hireing_employees(self):
        self.team3.hire_employee(self.intern1)
        self.assertEqual(self.team1.company, self.team3.company)  
        self.assertEqual(self.team1.employees, self.team3.employees)  
 
    def test_firing_employees(self):
        self.team1.fire_employee(self.intern1)
        self.assertEqual(self.team1.company, self.team3.company)  
        self.assertEqual(self.team1.employees, self.team3.employees)  
 
    def test_empty_team(self):
        empl = []
        t = Team("Google",empl)
        self.assertEqual(0, t.total_salaries())  

if __name__ == '__main__':
    unittest.main()