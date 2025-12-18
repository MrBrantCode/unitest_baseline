"""
QUESTION:
Develop a function `validate_IP(ip)` that takes a string `ip` as input and returns a string indicating whether the input is a valid IPv4 address or not. The function should check if the input string contains exactly four parts separated by dots and each part is a digit between 0 and 255 (inclusive).
"""

def validate_IP(ip):
    parts = ip.split(".")
    
    # checking if the length of the IP address is correct
    if len(parts) != 4:
        return "Invalid IP address"
    
    for part in parts:
        # checking if each part of the IP address is a number 
        # and if it's between 0 and 255
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return "Invalid IP address"
        
    return "Valid IP address"