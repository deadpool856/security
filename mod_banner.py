import socket

def checkPort(target, port):
    """
    Attempt to open a socket based connection to a host and port.

    If the port is open on the target, return True, and try to identify
    if it's an HTTP server.
    Otherwise, return False.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)  # Set a timeout for the connection attempt (2 seconds)

    try:
        sock.connect((target, port))
        banner = sock.recv(1024).decode("utf-8")  # Grab 1024 bytes of data and decode it to a string

        if "HTTP" in banner:
            return True, "Web server detected: " + banner
        else:
            return True, "Non-Web server detected: " + banner
    except (ConnectionRefusedError, socket.timeout):
        return False, None

if __name__ == "__main__":
    target = "127.0.0.1"
    common_web_ports = [80, 8080, 8000]

    for port in common_web_ports:
        isOpen, banner = checkPort(target, port)
        if isOpen:
            print(f"Port {port} is open. {banner}")
        else:
            print(f"Port {port} is closed.")
