"""
QUESTION:
Create a function `is_valid_ipv4_address` that takes a string as input representing an IP address. The function should return `True` if the IP address is valid, "Global Unicast" if it belongs to a globally routable network, "Private Use" if it belongs to a private network range, "Reserved" if it belongs to a reserved network range, and "Unknown" if it does not belong to any specified network ranges. A valid IPv4 address consists of four numbers (each ranging from 0 to 255) separated by periods. If the input string is not a valid IPv4 address, the function should return `False`.
"""

def is_valid_ipv4_address(address):
    # Split the address into four numbers
    numbers = address.split('.')

    # Check if the address consists of four numbers
    if len(numbers) != 4:
        return False

    # Check if each number is a valid integer between 0 and 255
    for number in numbers:
        try:
            if not 0 <= int(number) <= 255:
                return False
        except ValueError:
            return False

    # Check if the address belongs to a reserved network range
    if 0 <= int(numbers[0]) <= 127:
        return "Reserved"
    elif 128 <= int(numbers[0]) <= 191:
        return "Reserved"
    elif 192 <= int(numbers[0]) <= 223:
        return "Private Use"
    elif 224 <= int(numbers[0]) <= 239:
        return "Reserved"
    elif 240 <= int(numbers[0]) <= 255:
        return "Reserved"
    elif address == "0.0.0.0":
        return "Reserved"
    elif address == "255.255.255.255":
        return "Reserved"
    else:
        return "Global Unicast"