"""
QUESTION:
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:


Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  


       1 is typically treated as an ugly number.
       n does not exceed 1690.
"""

def find_nth_ugly_number(n: int) -> int:
    if n <= 0:
        return None
    
    ugly_numbers = [1]
    idx2, idx3, idx5 = 0, 0, 0
    
    while len(ugly_numbers) < n:
        next_ugly = min(ugly_numbers[idx2] * 2, ugly_numbers[idx3] * 3, ugly_numbers[idx5] * 5)
        ugly_numbers.append(next_ugly)
        
        if next_ugly == ugly_numbers[idx2] * 2:
            idx2 += 1
        if next_ugly == ugly_numbers[idx3] * 3:
            idx3 += 1
        if next_ugly == ugly_numbers[idx5] * 5:
            idx5 += 1
    
    return ugly_numbers[n - 1]