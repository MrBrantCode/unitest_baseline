"""
QUESTION:
Write a function `parse_ip_address` that takes an IP address as a string and returns the sum of the binary representations of its octets. The IP address is in the format of four numbers separated by dots, and each number is between 0 and 255. The binary representation of each octet should be calculated without leading zeros.
"""

def parse_ip_address(ip_address):
    octets = ip_address.split('.')
    binary_sum = 0
    for octet in octets:
        binary_octet = bin(int(octet))[2:]  # Convert octet to binary representation
        binary_sum += int(binary_octet, 2)  # Sum the binary value of each octet
    return binary_sum