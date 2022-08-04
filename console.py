import time

chars = 'ABCDEF'
loop = range(1, len(chars) + 1)

LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'


def clear_line(n=1):
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(n):
        print(LINE_UP, end=LINE_CLEAR)


print('a')
print('b')
print('c')
time.sleep(1)
clear_line(2)

print('d')
print('e')
print('f')