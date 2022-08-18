# Python program showing
# abstract base class work

from abc import abstractmethod, ABC


# abstract class syntax
class Alive(ABC):

    @abstractmethod
    def move(self):
        pass


# Human extends Alive
class Human(Alive):

    def move(self):
        super(Human, self).move()
        print("I can walk and run")


class Snake(Alive):

    def move(self):
        print("I can crawl")


class Dog(Alive):

    def move(self):
        print("I can bark")


class Lion(Alive):

    def move(self):
        print("I can roar")


# A = Alive()
# A.move()

# Driver code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()
