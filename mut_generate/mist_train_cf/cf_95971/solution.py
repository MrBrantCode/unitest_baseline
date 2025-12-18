"""
QUESTION:
Create a function called `parse_ip_addresses` that takes a string containing one or more IP addresses separated by commas. The function should return a list of IP addresses without delimiters and periods. Each IP address in the input string should be validated to be within the range of 0.0.0.0 to 255.255.255.255. If an invalid IP address is encountered, it should be ignored. The input string may contain whitespace characters, which should be ignored.
"""

def parse_ip_addresses(ip_string):
    ip_list = [ip.strip() for ip in ip_string.split(",")]
    valid_ips = []
    
    for ip in ip_list:
        # Remove whitespace characters
        ip = ip.replace(" ", "")
        
        # Split IP address into octets
        octets = ip.split(".")
        
        # Check if IP address has 4 octets
        if len(octets) != 4:
            continue
        
        # Check if each octet is a valid integer and within the range of 0 to 255
        try:
            valid_octets = [str(int(octet)) for octet in octets if 0 <= int(octet) <= 255]
        except ValueError:
            continue
        
        # Check if all octets were valid integers and within the range
        if len(valid_octets) != 4:
            continue
        
        # Construct valid IP address without delimiters
        valid_ip = "".join(valid_octets)
        
        valid_ips.append(valid_ip)
    
    return valid_ips