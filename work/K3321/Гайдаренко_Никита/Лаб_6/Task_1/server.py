import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    udata = data.decode("utf-8")
    print(f"Полученно сообщение от {str(addr)}: {udata}")

    response = "Hello, client"
    conn.send(response.encode("utf-8"))

conn.close()