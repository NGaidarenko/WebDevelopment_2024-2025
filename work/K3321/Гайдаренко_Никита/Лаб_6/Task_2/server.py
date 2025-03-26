import socket
import signal
import sys

def calculate_trapezoid_area(base1, base2, height):
    """Вычисляет площадь трапеции по формуле: S = (a + b) * h / 2"""
    area = (base1 + base2) * height / 2
    return f"Площадь трапеции с основаниями {base1} и {base2} и высотой {height} равна: {area:.2f}"

def shutdown(signum, frame):
    print("\nЗакрываем сервер...")
    server_socket.close()
    sys.exit(0)

# Настройка обработки Ctrl+C
signal.signal(signal.SIGINT, shutdown)

# Создание и настройка сокета
server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 9090))
server_socket.listen(1)

print("Сервер вычисления площади трапеции запущен на порту 9090. Для остановки нажмите Ctrl+C")

while True:
    client_socket, addr = server_socket.accept()
    try:
        # Получаем данные от клиента
        data = client_socket.recv(1024).decode()
        
        # Парсим входные параметры (два основания и высоту)
        base1, base2, height = map(float, data.split(','))
        
        # Вычисляем площадь
        result = calculate_trapezoid_area(base1, base2, height)
        
        # Отправляем результат клиенту
        client_socket.send(result.encode())
    except ValueError:
        error_msg = "Ошибка: неверный формат данных. Ожидается: base1,base2,height"
        client_socket.send(error_msg.encode())
    finally:
        client_socket.close()