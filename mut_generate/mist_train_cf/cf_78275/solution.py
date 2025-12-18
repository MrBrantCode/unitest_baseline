"""
QUESTION:
Develop a function `find_numeric_palindromes(n)` that returns a list of numeric palindromes within the range of 1 and a specified integer `n`. The function should recognize numbers that remain the same when their digits are reversed, and it should include the specified integer `n` in the range if it is a palindrome itself. The function should be able to handle any positive integer `n` as input.
"""

def find_numeric_palindromes(n):
    def is_palindrome(number):
        return str(number) == str(number)[::-1]

    palindromes = []
    for num in range(1, n+1):
        if is_palindrome(num):
            palindromes.append(num)
    return palindromes