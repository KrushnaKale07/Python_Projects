class Students_Result:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f'Hi {self.name}')
        print(f'Your marks are {self.marks}')

    def grade(self):
        if self.marks>=60:
            print('You got first class')
        elif self.marks>=50:
            print('You got second class')
        elif self.marks>=35:
            print('You got third class')
        else:
            print('You are fail')

n = int(input('Enter number of students'))
for i in range(n):
    name = input('Enter Name')
    marks = int(input('Enter Marks'))
    s = Students_Result(name, marks)
    s.display()
    s.grade()
    print()
