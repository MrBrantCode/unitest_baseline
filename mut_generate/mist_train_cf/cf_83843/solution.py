"""
QUESTION:
Design a function called `create_server_socket` that creates a server socket using the Secure Sockets Layer (SSL) protocol. The function should be able to handle potential anomalies and system failures, ensuring consistent reliability. The function should also be structured to allow for future growth and upkeep. The function should take in a host and port as parameters and return the created server socket. The SSL wrapper and client data handling functions are provided, but you need to design the server socket creation function to work with these functions.
"""

def create_server_socket(host='localhost', port=12345):
    """
    Creates a server socket using the Secure Sockets Layer (SSL) protocol.

    Args:
    host (str): The host IP address. Defaults to 'localhost'.
    port (int): The port number. Defaults to 12345.

    Returns:
    socket: The created server socket.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Starting server on', host, port)
    sock.bind((host, port))
    return sock