import socket

print("Mantan Nagpurkar")
print("Enrollment Number = 190130107071\n")

s = socket.socket()
host = input(str("please enter the host address of the sender : "))
port = 8080
s.connect((host, port))
print("Connected....")

client_message = ""
while client_message != 'exit':
    client_message = input("client : ")
    s.send(client_message.encode())
    server_message = s.recv(1024)
    print("server : ", server_message.decode())

s.close()
print("Disconnection.......")

