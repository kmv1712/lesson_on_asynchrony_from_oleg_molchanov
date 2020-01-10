# Работает асинхроно в одном потоке
import socket
from select import select

# select системная функция определяющая состояние файловых объектов
# В Unix системах все элементы являются файлами, каждый запущеный процесс это тоже файлы
# select работает с фалами у которых есть .fileno()
# Файловый дескриптов это номер файла
# select мониторит изминение файловых объектов в том числе и сокетов
# на вход select получает три списка  с файловыми дескрипторами
# Первый список объекты за которыми надо наблюдать когда они станут доступны для чтение
# Второй список объекты за которыми надо наблюдать когда станут доступны для записи
# Третий список объектов с ошибками

to_monitor = []

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

# Пока один ждет другой готов
# Определить какие сокеты готовы для чтения записи
# Описать механизм переключения


def accept_connection(server_socket):
    """ Принимает серверный сокет """
    # Метод accept() принимает входящее подключение, он читает данные из входящего буфера и если на вход пришло что-то
    # какое-то подлючение то метод accept возвращает нам кортеж с двумя элементами первый это socket, второй элемент
    # это адрес.
    client_socket, addr = server_socket.accept()
    print('Connection from', addr)
    to_monitor.append(client_socket)


def send_message(client_socket):
    # Должны дождаться от клиента какого-то сообщения
    # Получаю сообщение от клиента и устанавливаю размер буфера 4 килобайта этого сообщения
    request = client_socket.recv(4096)

    # Условие для прерывания цикла
    if request:
        response = 'Hello world\n'.encode()
        client_socket.send(response)
    else:
        # encode переводит строку в bytes
        client_socket.close()

# К клиенту можно подключится через бразер или например в командной строке ввести nc localhost 5000
# Возможность передовать контроль выполнения программы и какой-то код менеджер
# Событийный цикл, кусок кода который решает, что нам делать дальше event loop
# Асинхроный код можно писать без использования стороних библиотек с помощью callback, генератор и корутин, асинкэвэйт


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])  # read, write, errors

        for sock in ready_to_read:
            if sock == server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


# Точка входа
if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
    # accept_connection(server_socket)


