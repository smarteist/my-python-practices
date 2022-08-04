# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep


def best_worst_price(list):
    inc = None
    prev = None
    records = [0, 0]
    for item in list:
        if prev is not None:
            if item < prev and inc is not None and inc:
                records[0] += 1
            if item > prev and inc is not None and not inc:
                records[1] += 1
            inc = item > prev
        prev = item
    # count the last record
    if inc:
        records[0] += 1
    else:
        records[1] += 1
    return records


def multiply(a, b):
    if a < 0 and b < 0:
        a = abs(a)
        b = abs(b)
    result = 0
    for i in range(max(a, b)):
        result += min(a, b)
    return result


def print_hi():
    for i in range(10):
        if i % 2 == 0:
            print(i)
    p = lambda x: x * x
    print(type(p))


def somefunc(*args, **kvargs):
    print(type(args))
    print(args)
    print(kvargs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(best_worst_price([5, 6, 7, 8, 7, 5, 4, 6, 7, 8, 9, 10, 4, 6, 4, 6, 4, 2, 1, 3, 6, 2, 2, 1]))
    # print(best_worst_price([/1, 2, 3, 2, 3]))
    somefunc("salam", "khobi?", key1="value1", key2="value2")
