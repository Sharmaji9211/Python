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