class Shape:
    def draw(self):
        print("Drawing shape")
class Circle(Shape):
    def area(self):
        print("area of circle")
class Square(Shape):
    def area(self):
        print("area of square")
c=Circle()
s=Square()        

c.draw()
c.area()

s.draw()
s.area()