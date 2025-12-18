"""
QUESTION:
Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit.
 

Example 1:
Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.


Example 2:
Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.


Example 3:
Input: 1000
Output: 262


 
Note:

1 <= N <= 10^9
"""

import math

def count_numbers_with_repeated_digits(N: int) -> int:
    NN = N
    dd = 0
    nums = []
    
    # Extract digits from N
    while NN:
        dd += 1
        nums.append(NN % 10)
        NN //= 10
    nums.reverse()
    
    numbers = 0
    
    # Calculate the number of valid numbers with unique digits for each digit length
    for i in range(dd - 1):
        numbers += 9 * (math.factorial(9) // math.factorial(9 - i))
    
    already_visited_digits = set()
    
    # Helper function to calculate factorial combinations
    def fac2(n, k):
        return math.factorial(n) // math.factorial(n - k)
    
    # Calculate the number of valid numbers with unique digits for the given N
    for i, n in enumerate(nums):
        k = 0
        for j in range(1 if i == 0 else 0, n + 1 if i == dd - 1 else n):
            if j in already_visited_digits:
                continue
            k += 1
        numbers += k * fac2(10 - i - 1, dd - i - 1)
        if n in already_visited_digits:
            break
        already_visited_digits.add(n)
    
    # The result is the total numbers less than or equal to N minus the numbers with unique digits
    return N - numbers