from socket import *
import time # for RTT

# IP and port number server
PING_Params = ("127.0.0.1", 12000)

client = socket(AF_INET, SOCK_DGRAM)

#for loop sending 10 UDP pings
for i in range(0, 5):
    message = f"PING {i} - hello world"
    try:
        #setting timeout to 1 so we throw an error is more than 1 sec
        client.settimeout(1) 
        #todo: start timer
        t0 = time.time()
        #send message to UDP server
        client.sendto(message.encode('utf_8'), PING_Params)
        #getting message if not more than 1 sec
        data , addr = client.recvfrom(1024)
        #calculate rtt
        rtt = (time.time()) - t0
        #print response and ttl
        print(f"Response: {data.decode('utf_8')} RTT: {rtt}") 
    except Exception as e:
        print(f"Request timed out")

#close client
client.close()