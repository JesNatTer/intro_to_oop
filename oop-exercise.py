import math


class Shapes:
    def __init__(self, name, sides):
        super().__init__(name, sides)
        self.name = name
        self.sides = sides

    def area(self):
        print("I am a: " + self.name + " I have " + self.sides + "sides")


obj_shape = Shapes("shape", "so many")
obj_shape.area()


class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1

    def area(self):
        result = self.length * self.width
        return result


obj_book = Rectangle(10, 20)
obj_screen = Rectangle(50, 120)
print("the are of the book is " + str(obj_book.area()))
print("The area of the screen is " + str(obj_screen.area()))


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = (self.radius**2) * math.pi
        return round(result, 2)


obj_plate = Circle(30)
print("Area of plate is : " + str(obj_plate.area()))


class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        result = (self.base * 1/2) * self.height
        return result


obj_triangle = Triangle(5, 8)
print("The area of the triangle is : " + str(obj_triangle.area()))
