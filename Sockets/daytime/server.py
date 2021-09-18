import socket
import datetime
ip = '127.0.0.1'
port = 5003
print("Mantan Nagpurkar")
print("Enrollment Number = 190130107071\n")
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen(5)
while True:
    print("Server waiting for connections.....")
    conn, addr = server_socket.accept()
    print(f"Client connected from {addr} at time {str([str(datetime.datetime.now())])}")
    while True:
        data = conn.recv(1024)
        if not data or data.decode('utf-8') == "END":
            break
        try:
            conn.send(bytes(f"Time from server : {str([str(datetime.datetime.now())])}",'utf-8'))
        except:
            print("Exited by the user")
    conn.close()
server_socket.close()


# filename = input(str("Please enter the filename of the file : "))
# file = open(filename, 'rb')
# file_data = file.read(1024)
# conn.send(file_data)


# print("Data has been transmitted successfully....")



