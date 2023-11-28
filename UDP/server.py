# import socket

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind(('localhost', 9999))

# print("UDP server is listening on port 9999")

# while True:
#     data, address = server_socket.recvfrom(1024)
#     server_socket.sendto(data, address)


import socket

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = 'localhost'
server_port = 12345

server_socket.bind((server_host, server_port))
print('Server is ready to receive data...')

data, client_address = server_socket.recvfrom(1024).decode()
numbers = list(map(int, data.split(',')))

average = calculate_average(numbers)

server_socket.sendto(str(average).encode(), client_address)

server_socket.close()
