"""
QUESTION:
You will be given a positive integer N. Your task is to find the smallest number greater than or equal to N that is a prime and a palindrome.
 
Example 1:
Input: N = 12
Output: 101
Example 2:
Input: N = 4
Output: 5
 
Your Task:
You don't need to read or print anything. Your task is to complete the function PrimePalindrome() which takes N as input parameter and returns the smallest number greater than equal to N that is prime and palindrome.
Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{6}
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def next_palindrome(num):
    for i in range(1, 10**6):
        s = str(i)
        ans = int(s + s[-2::-1])
        if ans >= num and is_prime(ans):
            return ans
        s = str(i)
        ans = int(s + s[::-1])
        if ans >= num and is_prime(ans):
            return ans

def find_smallest_prime_palindrome(N):
    if N == 1 or N == 4 or N == 6:
        return N + 1
    elif N == 2 or N == 3 or N == 5 or N == 7:
        return N
    else:
        return next_palindrome(N)