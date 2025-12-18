"""
QUESTION:
Create a function named `sum_palindromes` that calculates the sum of numeric palindromes within the range of 1 to a given integer `n`. The function should return the sum of all numeric palindromes within this range, including `n` itself if it is a palindrome.
"""

def sum_palindromes(n):
    palindromes = []
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]: 
            palindromes.append(i)  

    return sum(palindromes) 