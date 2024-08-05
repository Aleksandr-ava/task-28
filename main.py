from time import sleep
from threading import Thread


def func1():
    for i in range(1, 11):
        sleep(1)
        print(i)


def func2():
    for k in 'abcdefghij':
        sleep(1)
        print(k)


odin = Thread(target=func1)
dva = Thread(target=func2)

odin.start()
dva.start()

odin.join()
dva.join()
