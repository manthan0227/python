import socket

print("Mantan Nagpurkar")
print("Enrollment Number = 190130107071\n")

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(5)
print(host)
print("Waiting for any incoming connections........")

conn, addr = s.accept()
server_message = ""
while server_message != "exit":
    client_message = conn.recv(1024)
    print("client : ", client_message.decode())
    server_message = input("server : ")
    conn.send(server_message.encode())

    # filename = input(str("Please enter the filename of the file : "))
    # file = open(filename, 'rb')
    # file_data = file.read(1024)
    # conn.send(file_data)

    # print("Data has been transmitted successfully....")

conn.close()
print("Disconnection......")
