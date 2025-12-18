"""
QUESTION:
Implement a function `validate_IPv4` that takes a string `IP` as input and returns a boolean value indicating whether the given string is a valid IPv4 address. The function should have a time complexity of O(1) and a space complexity of O(1). A valid IPv4 address consists of four decimal numbers separated by periods, where each decimal number is between 0 and 255 (inclusive), and does not have leading zeros.
"""

def validate_IPv4(IP: str) -> bool:
    IP = IP.strip()
    
    if len(IP) < 7 or len(IP) > 15:
        return False
    
    count = 0
    number = 0
    dotCount = 0
    
    for c in IP:
        if c.isdigit():
            number = number * 10 + int(c)
        elif c == '.':
            dotCount += 1
            if number < 0 or number > 255 or str(number) != str(number).lstrip('0') or (len(str(number)) > 1 and str(number)[0] == '0'):
                return False
            number = 0
        else:
            return False
    
    if number < 0 or number > 255 or str(number) != str(number).lstrip('0') or (len(str(number)) > 1 and str(number)[0] == '0'):
        return False
    
    if dotCount != 3:
        return False
    
    return True