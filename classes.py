# task 1
class Square:
    def __init__(self, side):
        self.n = None
        self.side = side

    def perimeter(self):
        summ = self.side * 4
        return summ

    def square(self):
        multiply = self.side ** 2
        return multiply

    def change_size(self, n):
        change = self.side * n
        return change


def compare_squares(square1, square2):
    area_difference = square1.square() - square2.square()
    return area_difference  # why is not inside the function


square1 = Square(5)
square2 = Square(3)

difference = compare_squares(square1, square2)
print(f"Площадь первого квадрата больше площади второго на: {difference}")

# looking for the primeter
perimeter_is = Square(5)
print(f"Периметр квадрата: {perimeter_is.perimeter()}")
square_is = Square(4)
print(f"the sqaure of the square is {square_is.square()}")


# task 2
class Cube:
    def __init__(self, height, width, length):
        self.height = height
        self.width = width
        self.length = length

    def volume(self):
        return self.width * self.height * self.length

    def little_squares(self):
        sides = [

            self.height * self.width,
            self.height * self.length,
            self.width * self.length
        ]
        return sides * 2


def piham_odno_v_drugoe(cube_one, cube_two):
    if cube_one.volume() > cube_two.volume():
        print('the second cube could be inside the first one')
    print('the volume of the second cube is higher, that is why it cannot be inside the first one')


cube_one = Cube(5, 5, 7)
cube_two = Cube(4, 6, 12)

piham_odno_v_drugoe(cube_one, cube_two)
print(f"The volume of the cube is: {cube_one.volume()}")
print(f"The sizes of the squares on the sides of the cube are: {cube_one.little_squares()}")

# task 3
import math


class Dots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def direction_from_zero(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @staticmethod
    def direction_between_each_other(dot1, dot2):
        return math.sqrt((dot1.x - dot2.x) ** 2 + (dot1.y - dot2.y) ** 2)


dot1 = Dots(3, 6)
dot2 = Dots(4, 7)
print(dot1.direction_from_zero())
print(dot2.direction_from_zero())
print(Dots.direction_between_each_other(dot1, dot2))
