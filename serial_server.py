import socket
import serial
import argparse
import threading


def serial_to_client(serial_dev, client_socket):
    with client_socket:
        print("serial to socket ready...\n")
        client_socket.sendall(b"serial to socket ready...\n")
        while True:
            data = serial_dev.readline()
            if not data:
                break
            # print(f"Serial to Socket: {data}")
            client_socket.sendall(data)  # Echo back the received data


def client_to_serial(client_socket, serial_dev):
    with client_socket:
        with client_socket:
            print("client to serial ready...\n")
            client_socket.sendall(b"client to serial ready...\n")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Socket to Serial: {data}")
                serial_dev.write(data)


def start_telnet_server(host='0.0.0.0', port=9988):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    # print(f"Telnet server listening on {host}:{port}")
    client_socket, addr = server.accept()

    return client_socket


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Argument Parsing.")
    parser.add_argument('--COM', type=str, required=True, help="COM name")
    parser.add_argument('--BAND', type=int, required=True, help="Baudrate")
    parser.add_argument('--PORT', type=int, required=True, help="PORT No.")
    args = parser.parse_args()
    # print(args.COM)
    # print(args.BAND)

    local_serial = serial.Serial(args.COM, args.BAND, timeout=None)
    local_socket = start_telnet_server(host='0.0.0.0', port=args.PORT)
    serial_to_client_handler = threading.Thread(target=serial_to_client, args=(local_serial, local_socket))
    serial_to_client_handler.daemon = True
    serial_to_client_handler.start()
    client_to_serial_handler = threading.Thread(target=client_to_serial, args=(local_socket, local_serial))
    client_to_serial_handler.daemon = True
    client_to_serial_handler.start()
    print("Server run...")

    while True:
        cmd = input()
        print(cmd, len(cmd))
        if cmd == "exit":
            print("will exit")
            exit()
        else:
            print("Invalid CMD...")
