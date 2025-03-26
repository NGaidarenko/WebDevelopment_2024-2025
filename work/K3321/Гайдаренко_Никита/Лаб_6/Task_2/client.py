import socket

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

client_socket = socket.socket()
client_socket.connect(('localhost', 9090))

data = f"{a},{b},{c}"
client_socket.send(data.encode())

result = client_socket.recv(1024).decode()
print(f"Результат: {result}")

client_socket.close()