class Area():
    PIE = 3.14

    def __init__(self,width,height):
        self.w = width
        self.h = height


    def square(self):
        result = self.w * self.h

        return result

    def triangle(self):
        result = (self.w * self.h)/2

        return result

    def circle(self):
        result = self.PIE * (self.w ** 2)

        return result

area = Area(10, 20)
print(area.square()) # 사각형의 넓이
print(area.triangle()) # 삼각형의 넓이
print(area.circle()) # 원의 넓이