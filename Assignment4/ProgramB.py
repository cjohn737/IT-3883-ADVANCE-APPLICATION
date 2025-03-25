import socket


client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 52221))

message = input("Enter a message: ")
client.send(message.encode())  # Send message

response = client.recv(1024).decode()  # Receive response
print("Server says:", response)

