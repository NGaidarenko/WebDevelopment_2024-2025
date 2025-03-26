import socket
import threading

clients = {}

def handle_client(client_socket, client_address):
    print(f"Подключен клиент: {client_address}")

    username = client_socket.recv(1024).decode('utf-8')
    clients[client_socket] = username
    print(f"Клиент {client_address} представился как {username}")

    broadcast(f"{username} присоединился к чату!", client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"Получено сообщение от {username}: {message}")

            broadcast(f"{username}: {message}", client_socket)
        except Exception as e:
            print(f"Ошибка при обработке сообщения от {username}: {e}")
            break

    del clients[client_socket]
    client_socket.close()
    print(f"Клиент {username} отключен")

    broadcast(f"{username} покинул чат.", client_socket)

def broadcast(message, sender_socket=None):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Ошибка при отправке сообщения клиенту: {e}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9090))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()