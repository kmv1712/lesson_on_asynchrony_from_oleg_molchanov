# asyncio предназначен для создания событийных циклов evenloop

# Event Loop:
#     corouyine > Task(Future)

'''
Асинхроная фунция отдает заглушку в js(promise), чтобы получить управление.
Дете получает обещание.

evenloop task корутин.
Е. корутина вызывает

asincio полноценый фреймворк.

Пример 2 функции
1) от 0 до беск
2) какое нибудь время

Делает корутину на основе генератора.

'''

'''
# python3.4

import asyncio
from time import time


@asyncio.coroutine
def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())

    yield from asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
'''

'''
В python3.5 
yield from заменили на await
@asyncio.coroutine заменили на async def 

import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
'''

'''
В python3.6
ensure_future уходит на задний план надо создавать через create_task 
@asyncio.coroutine заменили на async def 


import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
'''

'''
В python3.7
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
Можно заменить на 
asyncio.run(main())
'''

import asyncio
from time import time


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())

    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())