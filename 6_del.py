# Делегирующий генератор - это генератор вызывающий другой.
# Подгенератор - это вызываемый генератор.
# Нужно когда один генератор разбить на несколько.
# Смысол в том, что полученые делегирующим результат, как то обработать.
# yield form не только заменяет цикл в делегирующем генераторе, который проворачивает подгенератор
# yield form берет под себя передачу данных в подгенератор, передачу исключений, передачу с помощью return результат
# yield form g в других языках await
# вызывающий код вынужден ожидать, когда подгенератор закончит работу
# подгенератор должен содержать механизм завершающий его работу, иначе делегирующий генератор будет навечно заблокирован.
# yield form илдид итерируемый объект
# Пример:
# def a():
#     yield from 'oleg'
# g = a()
# next(g)
# o

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print('Ku-Ku!!!')
            break
        else:
            print('-----------', message)
    return 'Returned from subgen()'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)