"""
QUESTION:
Create a function `append_zeros(string, num_chars)` that appends a number of zeros to the end of the given string up to a maximum number of characters, where the maximum number of characters is a prime number between 1000 and 10,000. The function should first validate if the given string is a valid email address (containing both "@" and "." characters) and if the maximum number of characters is a prime number within the specified range. If any validation fails, return an error message.
"""

import math

def append_zeros(string, num_chars):
    if num_chars < 1000 or num_chars > 10000:
        return "Invalid number of characters"

    if "@" not in string or "." not in string:
        return "Invalid email address"

    if math.sqrt(num_chars) == int(math.sqrt(num_chars)) or num_chars < 2:
        return "Invalid number of characters"
    for i in range(2, int(math.sqrt(num_chars)) + 1):
        if num_chars % i == 0:
            return "Invalid number of characters"

    return string + "0" * (num_chars - len(string))