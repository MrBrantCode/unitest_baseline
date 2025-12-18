"""
QUESTION:
Create a function `parse_ip_addresses` that takes a string containing one or more IP addresses separated by commas, with possible whitespace characters. The function should return a list of valid IP addresses without delimiters and periods. Each IP address should be validated to be within the range of 0.0.0.0 to 255.255.255.255. If an invalid IP address is encountered, it should be excluded from the result.
"""

def parse_ip_addresses(ip_string):
    ip_list = [ip.strip() for ip in ip_string.split(",")]
    valid_ips = []
    
    for ip in ip_list:
        ip = ip.replace(" ", "")
        octets = ip.split(".")
        
        if len(octets) != 4:
            continue
        
        try:
            valid_octets = [str(int(octet)) for octet in octets if 0 <= int(octet) <= 255]
        except ValueError:
            continue
        
        if len(valid_octets) != 4:
            continue
        
        valid_ip = "".join(valid_octets)
        valid_ips.append(valid_ip)
    
    return valid_ips