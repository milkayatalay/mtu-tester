#!/usr/bin/env python3

import socket
import sys

def main():
    if len(sys.argv) == 3:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Run like : python3 listener.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
        exit(1)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ip, port)
    s.bind(server_address)
    print("Do Ctrl+c to exit the program")

    while True:
        print("####### Server is listening #######")
        data, address = s.recvfrom(4096)
        print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")


if __name__ == '__main__':
    main()

