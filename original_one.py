import socket

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
    print('Before .accept()')
    # Серверный сокет описали надо описать клиенский сокет

    # Метод accept() принимает входящее подключение, он читает данные из входящего буфера и если на вход пришло что-то
    # какое-то подлючение то метод accept возвращает нам кортеж с двумя элементами первый это socket, второй элемент
    # это адрес.
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)

    # Должны дождаться от клиента какого-то сообщения
    while True:
        print('Before .recv()')
        # Получаю сообщение от клиента и устанавливаю размер буфера 4 килобайта этого сообщения
        request = client_socket.recv(4096)

        # Условие для прерывания цикла
        if not request:
            break
        else:
            # encode переводит строку в bytes
            response = 'Hello world\n'.encode()
            client_socket.send(response)

    print('Outside inner while loop')
    client_socket.close()
# К клиенту можно подключится через бразер или например в командной строке ввести nc localhost 5000
# Возможность передовать контроль выполнения программы и какой-то код менеджер
# Событийный цикл, кусок кода который решает, что нам делать дальше event loop
# Асинхроный код можно писать без использования стороних библиотек с помощью callback, генератор и корутин, асинкэвэйт
