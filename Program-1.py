class Calculator:
    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2
    def operation(self, op):
        if op == '+':
            print(self.add())
        elif op == '-':
            print(self.subtract())
        elif op == '*':
            print(self.multiply())
        elif op == '/':
            print(self.divide())
        else:
            print("Enter valid operation")
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2
a, b= map(int, input().split())
op = input()
Calc = Calculator(a, b)
Calc.operation(op)
