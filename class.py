# class Student :
#     name= "Shivam"
#     age=24
#     add="Bareilly"
# s1=Student()
# print(s1.name)
# print(s1.age)
# print(s1.add)


class Student1 :
    def __init__(self,fullname):
        self.name = fullname
        print("Adding new student in Database...")

s1=Student1("Shivam")
print(s1.name)

s2=Student1("Kapil")
print(s2.name)


class student2():
    def __init__(self,name,phy,maths,english):
        self.name=name
        self.phy=phy
        self.maths=maths
        self.english=english
    def average(self):
        print((self.phy+self.english+self.maths)/3)

s1=student2("ShivamSharma",80,75,95)
s1.average()

class Student:
    name = "Shivam"
    age = 24

s1 = Student()

print(s1.name)
print(s1.age)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Shivam", 24)

print(s1.name)
print(s1.age)


class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(self.name, "is studying")

s1 = Student("Shivam")

s1.study()


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

c = Calculator()

print(c.add(10, 5))
print(c.subtract(10, 5))


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Shivam", 85)

s1.display()