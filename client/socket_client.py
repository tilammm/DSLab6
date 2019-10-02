import socket
from threading import Thread
import sys
import os.path

def main():
    port = int(sys.argv[3])  # Reserve a port for your service every new transfer wants a new port or you must wait.
    sock = socket.socket()  # Create a socket object
    host = str(sys.argv[2])  # Get local machine name
    sock.connect((host, port))
    filename = str(sys.argv[1])
    sock.send(filename.encode())
    f = open(str(sys.argv[1]), 'rb')
    size = os.path.getsize(sys.argv[1])
    bytes_transported = 1024
    percent = 0
    byte = f.read(1024)
    print(sock.recv(1024).decode())
    while byte:
        if bytes_transported * 100 // size > percent:
            percent = bytes_transported * 100 // size
            sys.stdout.flush()
            sys.stdout.write(f'\r{percent}%')
        bytes_transported += 1024
        sock.send(byte)
        byte = f.read(1024)
    f.close()
    print('End')
    sock.close()


if __name__ == "__main__":
    main()