"""
QUESTION:
You are given an integer n where 1 <= n <= 10^9. Create a function named reorderedPowerOf2(n) that determines if the digits of n can be rearranged to form a power of 2, ensuring the leading digit is not zero. The function should return a tuple of three values: 
1. A boolean indicating whether the rearrangement is possible.
2. The rearranged number that is a power of 2 (or -1 if no such rearrangement exists).
3. The minimum number of steps (swaps of two digits) required to reach the rearranged number from the original number (or -1 if no such rearrangement exists).
"""

from collections import Counter

def reorderedPowerOf2(n):
    strn = str(n)
    n_digits = len(strn)
    
    # check if the given number is already a power of 2
    if n & (n-1) == 0 and n != 0:
        return True, n, 0
    else:
        # creating list of all possible powers of 2 with same number of digits
        power_of_2_list = [2**i for i in range(31) if len(str(2**i)) == n_digits]
        
        # comparing each power of 2 with the given number
        for i in power_of_2_list:
            if Counter(strn) == Counter(str(i)):
                return True, i, calculate_steps(strn, str(i))
        
        return False, -1, -1

def calculate_steps(n, i):
    n_len, i_len = len(n), len(i)
    count_steps = 0
    for j in range(n_len):
        if n[j] != i[j]:
            indx_i = i[j:].index(n[j])
            i_list = list(i)
            i_list[j], i_list[j+indx_i] = i_list[j+indx_i], i_list[j]
            i = "".join(i_list)
            count_steps += 1
    return count_steps