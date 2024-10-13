# OOP modde kisu common fitured ace  shegolo hole
"""
1. Class
2. Object
3. Inheritance
4. Abstraction
5. Encapsulation
6. Polymorphism

"""

# inheritance = akti class ar boisisto k onno class niye jawa
#Parent class, Super class, Base class --> Phone
# Chile class , sub class, Derived class --> Samsung


# class Phone:
#     def call(self):
#         print("you can call")
#     def message(self):
#         print("You can message ")
#
#
# class Samsung(Phone):
#     def photo(self):
#         print("you can take photo")
#
# s = Samsung()
# s.message()
# s.call()
# s.photo()
# print(issubclass(Samsung, Phone))

# # shape ta hocce akta template ata onno class gola use korbe
# class Shape :
#     def __init__(self, dim1, dim2):
#         self.dim1 = dim1
#         self.dim2 = dim2
#
#     def area(self):
#         print("I am area method of shape class")
#
# class Triangle(Shape) :
#     def area(self):
#         area = 0.5 * self.dim1 * self.dim2
#         print("area of triangle : ", area)
#
# class Rectangle(Shape) :
#     def area(self):
#         area = self.dim1 *self.dim2
#         print("Area of Rectangle : ",area)
#
#
#
# t1 = Triangle(20, 39)
# t1.area()
#
# r1 = Rectangle(20, 39)
# r1.area()

# # inheritance 3 pokar :
# 1. Hierarchical Inheritance -- uporar emaple ta
# 2. Multi-Level Inheritance
# 3. Multiple Inheritance

# multi-level
class A :
    def display(self):
        print(" I am inside A class ")        
class B :
    def display(self):
        print(" I am inside B class")

class C(A, B) : # je class ta first a thakbe oita priroti beshi thakbe
    def display(self):
        super().display()


ob1 = C()
ob1.display()













































