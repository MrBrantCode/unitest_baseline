"""
QUESTION:
Create a function is_lychrel(n) that determines whether a number n is a Lychrel number or not. The function should iterate over the process of reversing and adding the number for up to 50 times and check whether the resulting number is a palindrome. If the resulting number is a palindrome within 50 iterations, the function should return False; otherwise, it should return True. The function should work with numbers below ten-thousand.
"""

def is_lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True