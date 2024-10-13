# abstractmethod ar class create korle tar objects create kora jabe na
from abc import ABC, abstractmethod

class Shape(ABC) :
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape) :
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("area of triangle : ", area)

class Rectangle(Shape) :
    def area(self):
        area = self.dim1 *self.dim2
        print("Area of Rectangle : ",area)


t1 = Triangle(20, 39)
t1.area()

r1 = Rectangle(20, 39)
r1.area()