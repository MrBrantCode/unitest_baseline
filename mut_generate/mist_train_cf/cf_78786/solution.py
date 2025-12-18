"""
QUESTION:
Define a function last_twelve_hex_digits that takes an integer n as input and returns the last twelve hexadecimal digits preceding the trailing zeroes in the factorial of n. The output should be a twelve-digit hexadecimal number with uppercase letters representing the digits A to F. The input will be a large integer, so the function should be designed to handle large numbers efficiently without direct computation of the full factorial.
"""

def last_twelve_hex_digits(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        while f % 16 == 0: 
            f //= 16       
        f %= 16**12     
   
    return hex(f)[2:].upper().zfill(12) 