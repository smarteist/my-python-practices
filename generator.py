import uuid
from time import sleep


def emmiter():
    while True:
        sleep(1)
        # looks like return keyword but with
        # listening option.
        yield uuid.uuid4()


def listen():
    for item in emmiter():
        print(item)


listen()
