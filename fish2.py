import socket

def checkPort(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    returnCode = sock.connect_ex((target, port))
    sock.close()

    if returnCode == 0:
        print(f"Port {port} is open.")
        return True
    elif returnCode == 111:
        print(f"Port {port} is closed.")
        return False

if __name__ == "__main__":
    target = "127.0.0.1"
    
    for port in range(0, 1025):
        isOpen = checkPort(target, port)
