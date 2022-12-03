# Group#: 15
# Student Names: Jose Pablo Palero and Brendan Lai

# UDPPingerServer.py 
# We will need the following module to generate randomized lost packets 
import random
import time 
from socket import * 

# Create a UDP socket  
# SOCK_DGRAM for UDP packets 
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket 
serverSocket.bind(('127.0.0.1', 12000)) 
print('Server is ready to receive...')

while True: 
    # Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024)

    # Rand between 5 and 50 ms for dealy
    rand_delay = random.randint(5, 50)/1000 #rand delay in ms
    time.sleep(rand_delay)

    # Randomly drop packet with a 10% prob otherwise respond
    rand = random.randint(0, 10) # Generate random number in the range of 0 to 10 
    # If rand is equal to 1 --> mimics 10% prob
    if rand == 1: 
        continue 
    # Otherwise, the server responds 
    # Replace hello world --> ditto
    message = (message.decode('utf_8')).split('-')[0] + "- ditto"
    print(message)
    serverSocket.sendto(message.encode('utf_8'), address)