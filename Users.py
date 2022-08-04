class Users:
    list = []

    def __init__(self, first_name, last_name):
        print('SUPER CLASS CALLED')
        self.first_name = first_name
        self.last_name = last_name


class Student(Users):
    def __init__(self, score, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.score = score
        print(f"{self.first_name} {self.last_name}")


std1 = Student(1, first_name="ali", last_name="alavi")
