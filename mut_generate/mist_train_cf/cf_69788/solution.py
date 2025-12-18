"""
QUESTION:
Design a function `mask_proxy_ip` that takes a proxy server IP address and a list of HTTP headers as input. The function should return a modified list of HTTP headers that removes the original client IP address from the 'X-Forwarded-For' header, effectively masking the client IP address. The modified list of HTTP headers should only include the IP address of the proxy server.
"""

def mask_proxy_ip(proxy_ip, http_headers):
    """
    This function masks the original client IP address from the 'X-Forwarded-For' header
    in a list of HTTP headers, replacing it with the IP address of the proxy server.

    Args:
        proxy_ip (str): The IP address of the proxy server.
        http_headers (dict): A dictionary of HTTP headers.

    Returns:
        dict: The modified HTTP headers with the client IP address masked.
    """
    
    # Check if 'X-Forwarded-For' header exists in the HTTP headers
    if 'X-Forwarded-For' in http_headers:
        
        # Split the 'X-Forwarded-For' header value by comma to separate IP addresses
        ip_addresses = http_headers['X-Forwarded-For'].split(',')
        
        # Remove leading and trailing whitespaces from each IP address
        ip_addresses = [ip.strip() for ip in ip_addresses]
        
        # Remove the original client IP address (the first IP address)
        ip_addresses = ip_addresses[1:]
        
        # Prepend the proxy server IP address to the list of IP addresses
        ip_addresses.insert(0, proxy_ip)
        
        # Join the IP addresses back into a string separated by comma
        http_headers['X-Forwarded-For'] = ','.join(ip_addresses)
    
    return http_headers