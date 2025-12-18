"""
QUESTION:
Write a function `calculate_xor(array)` that takes an array of integers as input and returns the sum of bitwise exclusive OR operations performed on every possible pair of integers within the array. The function should consider the bitwise XOR operation at each bit position (up to 31 positions) and calculate the aggregate sum.
"""

def calculate_xor(array):
    sum = 0
    n = len(array)

    for i in range(0,32):
        cnt = 0
        for j in range(0,n):
            if((array[j] & (1 << i))):
               cnt += 1

        sum += cnt * (n-cnt) * 2
    return sum