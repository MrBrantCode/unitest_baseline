"""
QUESTION:
Implement a function `largest_prime_palindrome_divisible_by_3` that takes a list of positive integers as input and returns the largest prime number that is a palindrome and is also divisible by 3. The solution must be implemented using recursion.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_prime_palindrome_divisible_by_3(lst):
    def helper(lst, current_max):
        if not lst:
            return current_max
        
        num = lst.pop()
        if num % 3 == 0 and is_palindrome(num) and is_prime(num):
            current_max = max(current_max, num)
        
        return helper(lst, current_max)
    
    return helper(lst, -1)