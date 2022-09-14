class Calc():
    def __init__(self) -> None:
        pass
    
    def set_number(self,a,b):
        try:
            self.a = int(a)
            self.b = int(b)
        except ValueError:
            print('숫자만 입력 가능합니다.')

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
        try:
            result = self.a / self.b
        except ZeroDivisionError:
            print('0으로 나눌 수 없습니다.')

        return result


calc = Calc()
calc.set_number(20,10)
print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값