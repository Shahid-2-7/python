class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self, a, b):
        print("Area of Retangle:", a * b)

class triangle():
    def area(self, a , b):
        print("Area of Triangle:", a * b / 2)

class square(shape):
    def area(self, a):
        print("Area of square:", a * a)

class circle(shape):
    def area(self, r):
        print("Area of Circle:", 3.14 * r * r)

s1 = rectangle()
s1.area(5,7)

s2 = triangle()
s2.area(3,4)

s3 = square()
s3.area(7)

s4 = circle()
s4.area(4)




             