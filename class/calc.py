class Calc():
    def __init__(self) -> None:
        pass
    
    def set_number(self,a,b):
        self.a = a
        self.b = b
    
    def plus(self):
        result = self.a + self.b
        
        return result

    def minus(self):
        result = self.a - self.b
    
        return result

    def multiple(self):
        result = self.a * self.b
    
        return result

    def divide(self):
        result = self.a / self.b
    
        return result

calc = Calc()
calc.set_number(20, 10)
print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값
