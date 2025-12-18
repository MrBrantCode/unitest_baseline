"""
QUESTION:
Construct a function `examine_string` that takes a string `text` as input. The function should find the index of the first occurrence of the digit '7' in the string that is not at the start or end of a sequence of digits and is surrounded by prime numbers. Non-digit characters in the string should be ignored. If no such '7' is found, the function should return -1.
"""

def examine_string(text):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    digits = [char for char in text if char.isdigit()]
    if len(digits) < 3:
        return -1
    for i in range(1, len(digits) - 1):
        if digits[i] == '7' and is_prime(int(digits[i - 1])) and is_prime(int(digits[i + 1])):
            return i
    return -1