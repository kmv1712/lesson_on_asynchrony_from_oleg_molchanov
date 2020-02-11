# async def не являются асинхроными сами по себе.

'''
1) Любая програма передавать управление
2) Событийный цикл
'''
from time import sleep

queue = []


def counter():
    counter = 0
    while True:
        print(counter)
        counter +=1
        yield


def printer():
    while True:
        counter = 0
        if counter % 3 == 0:
            print('Bang!')
        counter += 1
        yield


def main():
    while True:
        g = queue.pop(0)
        next()
        queue.append(g)
        sleep(0.5)


if __name__ == '__main__':
    g1 = counter()
    queue.append(g1)
    g2 = printer()
    queue.append(g2)
    main()
