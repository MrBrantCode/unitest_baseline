"""
QUESTION:
Create a function named "digits" that takes a positive integer n as input. The function should return the sum of the even digits of n plus the product of its odd digits. If n has only even digits, return the product of the first half of these digits. If n consists only of odd digits, return the sum of the first half.
"""

def digits(n):
    # convert the integer into a list of its digits
    n = [int(i) for i in str(n)]
    
    # separate even and odd digits
    evens = [i for i in n if i % 2 == 0]
    odds  = [i for i in n if i % 2 != 0]
    
    # error checking in case the input number only has even or odd digits
    if len(odds) == 0:
        half = len(evens) // 2
        product = 1
        for i in range(half):
            product *= evens[i]
        return product
    elif len(evens) == 0:
        half = len(odds) // 2
        return sum(odds[:half])
    else:
        # compute the product of odd digits and the sum of even ones
        return sum(evens) + (eval('*'.join(str(i) for i in odds)))