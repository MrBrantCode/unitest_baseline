"""
QUESTION:
Create a function named `perfect_palindrome` that takes an integer `n` as input and returns a list of all numbers from 1 to `n` that are both perfect numbers and palindromes. A perfect number is a positive integer that is equal to the sum of its proper divisors, and a palindrome is a number that remains the same when its digits are reversed. The function should be optimized to handle inputs up to 10^5.
"""

def perfect_palindrome(n):
    result = []
    for i in range(1, n+1):
        sum1 = 0
        temp = i
        if str(i) == str(i)[::-1]:
            for j in range(1, i):
                if i % j == 0:
                    sum1 += j
            if sum1 == i:
                result.append(i)
    return result