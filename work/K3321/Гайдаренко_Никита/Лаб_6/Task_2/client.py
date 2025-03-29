import socket

a = float(input("Введите основание 1: "))
b = float(input("Введите основание 2: "))
c = float(input("Введите высоту: "))

client_socket = socket.socket()
client_socket.connect(('localhost', 9090))

data = f"{a},{b},{c}"
client_socket.send(data.encode())

result = client_socket.recv(1024).decode()
print(f"Результат: {result}")

client_socket.close()