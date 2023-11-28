import socket

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = 'localhost' 
server_port = 12345 

server_socket.bind((server_host, server_port))

server_socket.listen(1)

client_socket, client_address = server_socket.accept()

data = client_socket.recv(1024).decode()

numbers = list(map(int, data.split(',')))
average = calculate_average(numbers)

client_socket.send(str(average).encode())

client_socket.close()
server_socket.close()
