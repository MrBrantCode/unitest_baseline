"""
QUESTION:
Define a function is_lychrel(n) that takes a non-negative integer n as input and returns True if n is a Lychrel number and False otherwise. A Lychrel number is a number that does not yield a palindrome when repeatedly reversed and added to itself for 50 iterations or less. If a palindrome is found in 50 iterations or less, return False. If no palindrome is found after 50 iterations, return True. The function should work for all non-negative integers n less than 10,000.
"""

def is_lychrel(n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    for i in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True