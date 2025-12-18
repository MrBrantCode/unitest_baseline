"""
QUESTION:
Implement a function `even_odd_count(num)` that takes an integer as input and returns a tuple representing the counts of even and odd digits within the input integer. The function should handle negative numbers and numbers with preceding zeros. Note that the function should consider '0' as an even digit.
"""

def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)): 
        if digit.isdigit():     
            if int(digit) % 2 == 0: 
                even_count += 1
            else:
                odd_count += 1
    return even_count, odd_count