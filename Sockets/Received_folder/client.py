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

    # filename = input(str("Please enter a filename for the incoming file : "))
    # file = open(filename, 'wb')
    # file_data = s.recv(1024)
    # file.write(file_data)
    # file.close()

    # print("File has been received successfuilyy.....")
    
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

s.close()
print("Disconnection.......")

