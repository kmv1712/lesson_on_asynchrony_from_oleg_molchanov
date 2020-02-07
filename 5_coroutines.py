# Корутины генератопы которые из вне получают данные
# from inspect import getgeneratorstate, библиотека, чтобы посмотреть в каком состояние генератор.
# throw(StopIteration)
# average() - создаст объект генератора
# coroutine - декоратор для инициализации генератора
# генераторы и корутины могут иметь return и возвращать некое значение.


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    x = 'Ready to acept message'
    message = yield x
    print('Subgen received', message)


class BlaBlaException(Exception):
    pass


@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except BlaBlaException:
            print('------------------------------')
            break
        else:
            count += 1
            summ += x
            average = round(summ/count)
    return average