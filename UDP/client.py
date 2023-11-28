# import socket

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send = "hello"
# client_socket.sendto(send.encode(), ('localhost', 9999))

# data, address = client_socket.recvfrom(1024)
# print("Received:", data)

# client_socket.close()


import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_host = 'localhost'
server_port = 12345

numbers = [10, 20, 30, 40]
data = ','.join(map(str, numbers))
client_socket.sendto(data.encode(), (server_host, server_port))

result, server_address = client_socket.recvfrom(1024)
print('Average:', result.decode())

client_socket.close()
