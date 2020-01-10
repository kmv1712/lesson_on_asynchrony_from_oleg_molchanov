# урок 3
# Особеность регестрировали сокеты вместе с сопровождающими данными


import socket
import selectors

# selectors - тоже самое, что select

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # Зарегистрирум серверный сокет
    # events событие которое нас интересует
    # data  любые связанные данные прим: сесии, id сесии и.т.д
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    # Зарегистрирум клиентский сокет
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        # Прежде чем закрыть надо снять с регистрации
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:
        # Получить выборку элементов готовых для чтения и записи
        events = selector.select()  # (key, events)

        # SelectorKey именнованый кортеж, (облегченый вариант класс), нужен чтобы связать между собой сокет, ожидаемые
        # события и данные
        # fileobj
        # events
        # data

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


# Точка входа
if __name__ == '__main__':
    server()
    event_loop()
    # accept_connection(server_socket)
