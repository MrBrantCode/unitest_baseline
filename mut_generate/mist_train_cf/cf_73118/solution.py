"""
QUESTION:
Write a function named `find_subnet` that takes an IP address as input and returns the default subnet mask based on the IP address class. The IP address should be in the format of four octets separated by periods (e.g., "192.168.1.1"). The function should return the subnet mask in the same format. Assume the IP address is valid and within the range of Class A, B, or C.
"""

def find_subnet(ip):
    ip_parts = ip.split('.')
    first_octet = int(ip_parts[0])

    # Identify the class based on the first octet
    if 1 <= first_octet <= 126:
        return "255.0.0.0" # Class A
    elif 128 <= first_octet <= 191:
        return "255.255.0.0" # Class B
    elif 192 <= first_octet <= 223:
        return "255.255.255.0" # Class C
    else:
        return "No default subnet mask" # Class D or E