import  socket


target_host = 'www.google.com'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

client.send(b'')
response = client.recv(4096)

print(response.decode())
client.close()
