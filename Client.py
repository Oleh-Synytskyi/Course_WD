import socket
import threading
import smtplib
from tkinter import *
import sys
import os



#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(2048)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break
#Get host and port
host = input("Host: ")
port = int(input("Port: "))
Name = input("Name: ")

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("============Welcome to server============")
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network

#Commands
while True:
        command = input('Input your command: ')
        if command == 'exit':
            sock.sendall(str.encode(command))
            sock.close()
        parameter = input("Input command parameters:")
        if command == 'ping':
            os.system('ping'+' ' + parameter)
        if command == 'echo':
            os.system('echo'+' ' + parameter)
        if command == 'dir':
            os.system('dir'+' ' + parameter)
        if command == 'exit':
            os.system('exit'+' ' + parameter)
        if command == 'msg':
            os.system('msg'+' ' + parameter)
        if command == 'start':
            os.system('start'+' ' + parameter)
        msg = input("Your message --> ")
        sock.sendall(str.encode(msg))




