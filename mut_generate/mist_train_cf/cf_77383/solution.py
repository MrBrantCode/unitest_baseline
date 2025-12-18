"""
QUESTION:
Create a function `isValidDecimal(s)` that checks if a given string `s` represents a decimal number with a precision of 2. The number should be positive, fall within a specific range between 0 and 1000 (exclusive), and not be a multiple of 10. The function should also handle potential leading and trailing whitespaces and remove any non-numeric characters before performing the checks. Additionally, the function should validate if the integral part of the decimal number is a prime number.
"""

import re

def isValidDecimal(s):
    # remove any non-numeric characters and trim whitespaces
    s = "".join(re.findall("\d+\.?\d*", s.strip()))

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    try: 
        num = float(s)
        # checking if the number num has 2 decimal places
        if not('.' in s and (len(s) - s.index('.') - 1) == 2):
            return False      
        else: 
             # check if it's a positive number within the range and not multiple of 10
             if 0 < num < 1000 and num % 10 != 0:
                 # check if the integral part is prime
                 return is_prime(int(num))
    except ValueError:
        return False