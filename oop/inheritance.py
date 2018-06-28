class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @staticmethod
    def is_U18(age):
        if age < 18:
            return True
        return False

class Student(Person):
    def __init__(self,name,school,age):
        self.name = name 
        self.school = school
        self.age = age


student1 = Student("Harry","TUES",15)
print(Student.is_U18(student1.age))
print(student1.is_U18(student1.age))