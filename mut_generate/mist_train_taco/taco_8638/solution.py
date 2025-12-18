"""
QUESTION:
Consider the sequence of numbers 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, ... In this sequence first we have the number 1, then the numbers from 1 to 2, then the numbers from 1 to 3 and so on. Your task is to find the N'th number in this sequence.
 
Example 1:
Input: N = 4
Output: 1
Explanation: 4'th number is 1. 
Ã¢â¬â¹Example 2:
Input: N = 14
Output: 4
Explanation: 14'th number is 4.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function get() which takes N as input and returns the answer.
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{10}
"""

from math import sqrt, floor

def find_nth_number_in_sequence(N: int) -> int:
    num = floor((sqrt(1 + 8 * N) - 1) / 2)
    if N == num * (num + 1) // 2:
        result = num
    else:
        result = N - num * (num + 1) // 2
    return result