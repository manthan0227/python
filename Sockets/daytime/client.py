import socket

ip = '127.0.0.1'
port = 5003

print("Mantan Nagpurkar")
print("Enrollment Number = 190130107071\n")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((ip, port))
data = "Hello Server...."

try:
    client_socket.send(data.encode('utf-8'))
    ser_data = client_socket.recv(1024)
    print(str(ser_data))

except KeyboardInterrupt:
    print("Exited by the user")
client_socket.close()
