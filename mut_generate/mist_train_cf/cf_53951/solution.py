"""
QUESTION:
Implement a function named `configure_android_emulator_proxy` to set up an Android Emulator behind a proxy that requires authentication. The function should take the following parameters: `proxy_ip`, `port`, `proxy_username`, and `proxy_password`. There are no specific restrictions on the return type of the function.
"""

def configure_android_emulator_proxy(proxy_ip, port, proxy_username, proxy_password):
    """
    Configures the Android Emulator behind a proxy that requires authentication.

    Parameters:
    proxy_ip (str): The IP address of the proxy server.
    port (int): The port number of the proxy server.
    proxy_username (str): The username for the proxy authentication.
    proxy_password (str): The password for the proxy authentication.

    Returns:
    str: A formatted proxy string.
    """
    proxy_string = f"http://{proxy_username}:{proxy_password}@{proxy_ip}:{port}"
    return proxy_string