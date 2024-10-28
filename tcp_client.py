import  socket


target_host = '192.168.122.164'
target_port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - IP4 адрес, SOCK_STREAM - TCP
client.connect((target_host, target_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
response = client.recv(4096)

print(response.decode())
client.close()

