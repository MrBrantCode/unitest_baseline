"""
QUESTION:
Write a function `parse_ip_address` that takes a string representing an IP address as input and returns the sum of the binary values of its octets. The function should split the IP address into octets using the dot as the delimiter, convert each octet to its binary representation, and then sum up the binary values.
"""

def parse_ip_address(ip_address):
    octets = ip_address.split('.')
    binary_sum = 0
    for octet in octets:
        binary_octet = bin(int(octet))[2:]  # Convert octet to binary representation
        binary_sum += int(binary_octet, 2)  # Sum the binary value of each octet
    return binary_sum