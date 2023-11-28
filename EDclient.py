import socket

def add_parity_bit(binary_string, parity):
    if parity == "even":
        return binary_string + calculate_parity_bit(binary_string)
    elif parity == "odd":
        return binary_string + "1" if calculate_parity_bit(binary_string) == "0" else "0"

def calculate_parity_bit(binary_string):
    count = 0
    for char in binary_string:
        if char == '1':
            count += 1
    return '1' if count % 2 != 0 else '0'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_ADDRESS = '127.0.0.1'
PORT = 1234
client_socket.connect((IP_ADDRESS, PORT))

message = input("Enter the message to be sent: ")
parity = input("Enter the parity type (even/odd): ")

message_with_parity_bit = add_parity_bit(message, parity)
client_socket.send(message_with_parity_bit.encode())

print(f"Sent message to server: {message_with_parity_bit}")

client_socket.close()
