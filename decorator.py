from datetime import datetime
from time import sleep


def log_time(func):  # that function itself
    def timer(n):  # and its argrument
        start = datetime.now()
        res = func(n)
        print(f"functions executed in {(datetime.now() - start).total_seconds()} seconds!")
        return res

    return timer


@log_time
def use_decorator(n):
    sleep(n)


use_decorator(2)
