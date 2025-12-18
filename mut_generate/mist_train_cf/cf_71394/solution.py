"""
QUESTION:
Given an arithmetic series with the formula a + (n-1)d, where a and d are positive integers and d is greater than 1, find the greatest potential value of m, where m is the number of distinct terms that can be selected with the same quantity of digits. The selected terms must be different, and the number of digits in each term must remain constant.
"""

def entrance(a, d):
    n = 1
    term = a
    m = 0
    digits = len(str(term))
    
    while len(str(term)) == digits:
        m += 1
        n += 1
        term = a + (n-1)*d
        
    return m