"""
QUESTION:
Write a function `is_valid_ipv4_address(ip_address: str) -> bool` that takes a string as input, determines if it is a valid IPv4 address or not, and returns a boolean result. The input string contains only digits and periods, is in the format "x.x.x.x", and does not have any leading or trailing spaces. Each integer x must be between 0 and 255. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def is_valid_ipv4_address(ip_address: str) -> bool:
    # Split the IP address by periods
    parts = ip_address.split(".")
    
    # Check if there are exactly 4 parts
    if len(parts) != 4:
        return False
    
    # Check if each part is a valid integer between 0 and 255
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255 or (len(part) > 1 and part[0] == "0"):
            return False
    
    return True