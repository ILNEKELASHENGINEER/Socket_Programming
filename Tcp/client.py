import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = 'localhost' 
server_port = 12345

client_socket.connect((server_host, server_port))

numbers = [10, 20, 30, 40]
data = ','.join(map(str, numbers))
client_socket.send(data.encode())

result = client_socket.recv(1024).decode()
print('Average:', result)

client_socket.close()
