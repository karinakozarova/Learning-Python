class Person:

    is_alive = True
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @staticmethod
    def is_U18(age):
        if age < 18:
            return True
        return False

    @classmethod
    def all_die(cls):
        cls.is_alive = False

    def print_kind():
        print("Person")

class Student(Person):
    def __init__(self,name,school,age):
        self.name = name 
        self.school = school
        self.age = age

    @staticmethod
    def print_kind():
        print("Student")

student1 = Student("Harry","TUES",15)
print(Student.is_U18(student1.age))
print(student1.is_U18(student1.age))

print(student1.is_alive)
Person.all_die()
print(student1.is_alive)

student1.print_kind()
Person.print_kind()