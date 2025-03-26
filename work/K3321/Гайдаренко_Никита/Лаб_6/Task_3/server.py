import socket

# Функция для загрузки HTML-файла
def load_html_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "<h1>Error: File not found</h1>"

# Функция для создания HTTP-ответа
def create_http_response(html_content):
    html_content_bytes = html_content.encode('utf-8')

    headers = "HTTP/1.1 200 OK\r\n"
    headers += "Content-Type: text/html\r\n"
    headers += f"Content-Length: {len(html_content_bytes)}\r\n"
    headers += f"Connection: close\r\n"
    headers += "\r\n"

    return headers + html_content

html_content = load_html_file("index.html")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

while True:
    client_socket, addr = server_socket.accept()

    response = create_http_response(html_content)

    client_socket.send(response.encode('utf-8'))

    client_socket.close()