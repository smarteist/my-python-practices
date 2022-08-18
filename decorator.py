from datetime import datetime
from time import sleep


def log_time(func):  # that function itself
    def mediator(*args, **kwargs):  # and its argrument
        # do something before that
        start = datetime.now()
        # call itself
        res = func(*args, **kwargs)
        # we have its return value and do smothing with it...
        print(f"The result was: {res}")
        print(f"functions executed in {(datetime.now() - start).total_seconds()} seconds!")
        # an then return it to user
        return res

    # docrator logic
    return mediator


@log_time
def use_decorator():
    sleep(1)
    return 'OK'


use_decorator()
