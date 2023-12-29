# Using instance method

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

obj1 = Student('Akshay',60)
obj2 = Student('Adi', 80)
obj1.display()
obj2.display()
