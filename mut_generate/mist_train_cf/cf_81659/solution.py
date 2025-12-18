"""
QUESTION:
Write a function `convert_ip(ip_address)` that takes a string representing an IP address in dot-decimal notation and returns its binary representation as a string. The function should validate the input IP address and return "Invalid IP address" if it is not a valid IP address. A valid IP address consists of four numbers separated by dots, each number being between 0 and 255 inclusive.
"""

def convert_ip(ip_address): 
    binary_ip = ''
    for i in ip_address.split('.'):
        # Check if each portion of IP is a number and is between 0 and 255.
        if not i.isdigit() or not 0 <= int(i) <= 255:
            return "Invalid IP address"
        binary_ip += format(int(i), '08b') + '.' 
    return binary_ip.rstrip('.')