import socket
from select import select

# Dabid Beazley
tasks = []

to_read = {}
to_write = {}


def server():
    # Обслуживать запросы пользователя.
    # AF_INET - ip протокол 4 версии.
    # socket.SOCK_STREAM - поддержка TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Таймаут 3 мин, чтобы использовать порт повторно определим следующие опции
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # к какому домену и порту привяжу серверный socket
    server_socket.bind(('localhost', 5000))
    # Должен указать серверному сокету, чтобы начал прослушивать буфер на предмет каких-то входящих подключений.
    server_socket.listen()

    # т.к. Отношение между клиентом и сервером это длительное отношение поэтому обычно используют бесконечный цикл
    while True:

        yield ('read', server_socket)
        # Метод accept() принимает входящее подключение, он читает данные из входящего буфера и если на вход пришло что-то
        # какое-то подлючение то метод accept возвращает нам кортеж с двумя элементами первый это socket, второй элемент
        # это адрес.
        client_socket, addr = server_socket.accept()  # read

        print('Connection from', addr)
        tasks.append(client(client_socket))


def client(client_socket):
    # Должны дождаться от клиента какого-то сообщения
    while True:
        yield ('read', client_socket)
        # Получаю сообщение от клиента и устанавливаю размер буфера 4 килобайта этого сообщения
        request = client_socket.recv(4096)  # read

        # Условие для прерывания цикла
        if not request:
            break
        else:
            # encode переводит строку в bytes
            response = 'Hello world\n'.encode()
            yield ('write', client_socket)
            client_socket.send(response)  # write

    client_socket.close()


def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)

            reason, sock = next(task)

            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('Done!')


tasks.append(server())
event_loop()
