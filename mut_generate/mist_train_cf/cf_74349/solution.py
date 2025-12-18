"""
QUESTION:
Create a function named "digits" that takes a positive integer n as input. The function should return the product of all odd digits in n and the sum of all even digits. However, if n consists only of even digits, return the product of the first half of the even digits. If n consists only of odd digits, return the sum of the first half of the odd digits.
"""

def entrance(n):
    n = [int(i) for i in str(n)]
    odd = [i for i in n if i % 2 != 0]
    even = [i for i in n if i % 2 == 0]

    if len(odd) == 0:  # all digits are even
        half = len(even) // 2
        product = 1
        for num in even[:half]:
            product *= num
        return product

    elif len(even) == 0:  # all digits are odd
        half = len(odd) // 2
        return sum(odd[:half])
        
    else:  # mix of odd and even digits
        product = 1
        for num in odd:
            product *= num
        return product + sum(even)