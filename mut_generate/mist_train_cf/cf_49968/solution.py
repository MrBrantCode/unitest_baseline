"""
QUESTION:
Implement a secure Web service solution for a publicly exposed production server that only allows access from a separate internal Web server. The solution should restrict access to the internal Web server only and prevent unauthorized access. Consider implementing one or more of the following methods: IP whitelisting, VPN, Mutual SSL, API keys, Web service authentication, firewall settings, and network segmentation.
"""

def restrict_access(whitelist_ips, client_ip):
    """
    Restricts access to the web service based on IP whitelisting.

    Args:
    - whitelist_ips (list): A list of allowed IP addresses.
    - client_ip (str): The IP address of the client requesting access.

    Returns:
    - bool: True if access is granted, False otherwise.
    """
    return client_ip in whitelist_ips