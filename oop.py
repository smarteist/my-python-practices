from abc import abstractmethod, ABC


class Shape:
    # CLASS WIDE STATIC LIST
    staticList = []

    def __init__(self):
        self.staticList.append(self)

    def getarea(self):
        pass

    @abstractmethod
    def getcircumference(self):
        pass


class Circle(Shape, ABC):

    def __init__(self, radius):
        super(Circle, self).__init__()
        self.radius = radius
        print(self.radius)


class Square(Shape, ABC):

    def __init__(self, width, height):
        super(Square, self).__init__()
        self.staticList.append(self)
        self.height = height
        self.width = width

    def getarea(self):
        return self.width * self.height


circle_1 = Circle(radius=2)
circle_2 = Circle(3)
circle_3 = Circle(3)
circle_4 = Circle(3)

sq = Square(2, 3)

print(sq.width)
print(sq.height)
print(circle_1.staticList)
print(sq.staticList)
print()
# print(type(circle_1))
# print(type(sq))
