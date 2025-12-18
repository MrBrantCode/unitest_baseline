"""
QUESTION:
In this problem you will be given a range 'n', and you are supposed to find all composite numbers within that range. Make your program efficient as time limit of the program is set to 1 second. Choose an efficient algorithm to find all the composite numbers within the range 0 to n.

Input

n - a single positive Integer.

Output

Space separated composite-numbers within the range of 0 and n.

Constrains

1 ≤ n ≤ 10000

SAMPLE INPUT
8

SAMPLE OUTPUT
4 6 8
"""

import math

def find_composite_numbers(n):
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return True
        return False
    
    composite_numbers = []
    for i in range(4, n + 1):
        if is_composite(i):
            composite_numbers.append(i)
    
    return composite_numbers