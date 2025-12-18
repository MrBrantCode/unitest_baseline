"""
QUESTION:
Write a function count_winning_n that takes two integers min and max as input and returns the number of integers n within the range min to max (inclusive) where the first competitor can strategically ensure a win. The first competitor can strategically ensure a win if and only if n is not a member of the geometric sequences n = 34k, n = 34k + 5, or n = 34k + 17, where k is a non-negative integer.
"""

def count_winning_n(min, max):
    total = 0
    for n in range(min, max+1):
        if n%34 != 0 and n%34 !=5 and n%34 != 17:
            total += 1
            
    return total