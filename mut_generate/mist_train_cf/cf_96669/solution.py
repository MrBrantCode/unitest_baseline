"""
QUESTION:
Write a function `is_valid_ipv4_address(address)` that takes a string `address` as input. The function should return `True` if the input string is a valid IPv4 address and `False` otherwise. If the input string is a valid IPv4 address, the function should also return a string indicating the type of network range it belongs to, which can be "Global Unicast", "Private Use", "Reserved", or "Unknown". The function should follow the IANA specifications for reserved network ranges.
"""

def is_valid_ipv4_address(address):
    # Split the address into four numbers
    numbers = address.split('.')

    # Check if the address consists of four numbers
    if len(numbers) != 4:
        return False, "Unknown"

    # Check if each number is a valid integer between 0 and 255
    for number in numbers:
        try:
            if not 0 <= int(number) <= 255:
                return False, "Unknown"
        except ValueError:
            return False, "Unknown"

    # Check if the address belongs to a reserved network range
    if 0 <= int(numbers[0]) <= 127:
        return True, "Reserved"
    elif 128 <= int(numbers[0]) <= 191:
        return True, "Reserved"
    elif 192 <= int(numbers[0]) <= 223:
        return True, "Private Use"
    elif 224 <= int(numbers[0]) <= 239:
        return True, "Reserved"
    elif 240 <= int(numbers[0]) <= 255:
        return True, "Reserved"
    elif address == "0.0.0.0":
        return True, "Reserved"
    elif address == "255.255.255.255":
        return True, "Reserved"
    else:
        return True, "Global Unicast"