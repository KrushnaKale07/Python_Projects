class Calculator:

    def __init__(self, num1, num2):

        self.num1=num1
        self.num2=num2

        print(self.add())
        print(self.sub())
        print(self.mul())
        print(self.div())
        print(self.floor_div())
        print(self.exponential())
        print(self.modulus())

    def add(self):
        return f'Addition of {self.num1} and {self.num2} is {self.num1+self.num2}'

    def sub(self):
        return f'Substraction of {self.num1} and {self.num2} is {self.num1-self.num2}'

    def mul(self):
        return f'Multiplication of {self.num1} and {self.num2} is {self.num1*self.num2}'

    def div(self):
        return f'Division of {self.num1} and {self.num2} is {self.num1/self.num2}'

    def floor_div(self):
        return f'Floor division of {self.num1} and {self.num2} is {self.num1//self.num2}'

    def exponential(self):
        return f'Exponential of {self.num1} and {self.num2} is {self.num1**self.num2}'

    def modulus(self):
        return f'Modulus of {self.num1} and {self.num2} is {self.num1%self.num2}'

obj = Calculator(20,10)
