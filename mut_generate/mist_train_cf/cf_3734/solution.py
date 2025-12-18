"""
QUESTION:
Create a function named `parse_ip_address` that takes an IP address as input. The function should split the IP address into its four octets, convert each octet to its binary representation using bitwise operations, and calculate the sum of all the binary values. The function should return the sum of binary values if the IP address is valid, and return an error message "Invalid IP address" if the IP address is invalid. A valid IP address should have exactly four octets, and each octet should be an integer between 0 and 255.
"""

def parse_ip_address(ip_address):
    octets = ip_address.split(".")
    if len(octets) != 4:
        return "Invalid IP address"
    
    binary_sum = 0
    for octet in octets:
        try:
            octet_int = int(octet)
            if octet_int < 0 or octet_int > 255:
                return "Invalid IP address"
            
            binary = bin(octet_int)[2:].zfill(8)
            binary_sum += int(binary, 2)
        except ValueError:
            return "Invalid IP address"
    
    return binary_sum