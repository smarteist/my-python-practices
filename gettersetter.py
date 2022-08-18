class Student:
    def __init__(self, name):
        self.thename = name

    @property
    def name(self):
        return self.thename

    @name.setter
    def name(self, name):
        self.thename = name

    @name.deleter
    def name(self):
        del self.thename


s = Student('Steve')
print(s.name)
s.name = 'Bill'
print(s.name)
del s.name
print('Property Successfully deleted')

try:
    s.name
except AttributeError as e:
    print(e)
