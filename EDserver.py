import random
import socket

def calculate_parity_bit(binary_string):
    count = 0
    for char in binary_string:
        if char == '1':
            count += 1
    return '1' if count % 2 != 0 else '0'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_ADDRESS = '127.0.0.1'
PORT = 1234
server_socket.bind((IP_ADDRESS, PORT))

server_socket.listen()

print(f"Server is listening on {IP_ADDRESS}:{PORT}")

client_socket, client_address = server_socket.accept()

print(f"Connection established with {client_address}")

data = client_socket.recv(1024).decode()
print(f"Received data from client: {data}")

message_bits = data[:-1]
received_parity_bit = data[-1]

error = input("Need to corrupt ? y/n : ")
if error == 'y':
    error_position = random.randint(0,len(message_bits))
    print("Flipping the bits at random index",error_position)
    if len(message_bits) > error_position:
        message_bits = message_bits[:error_position] + ('0' if message_bits[error_position] == '1' else '1') + message_bits[error_position+1:]
        print("Corrupted data : ",message_bits)
calculated_parity_bit = calculate_parity_bit(message_bits)

if received_parity_bit == calculated_parity_bit:
    print("Message received without any errors")
else:
    print("Error detected in received message")

client_socket.close()
server_socket.close()
