# Program Name: Assignment4.py
# Course: IT3883/Section 01
# Student Name: Caitlin Johnson
# Assignment Number: Lab#4
# Due Date: 03/24/ 2025
# Purpose: What does the program do (in a few sentences)? This program creates a simple way for two computers to talk to each other over a network.
# List Specific resources used to complete the assignment. YouTube.com, realpython.com, GeeksForGeeks.com

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 52221))
server.listen()

client, addr = server.accept()
print("Client connected.")

data = client.recv(1024).decode()  # Receive message
client.send(data.upper().encode())  # Convert to uppercase


response = client.recv(1024).decode()  # Receive response
print("Server says:", response)