"""
QUESTION:
Define a function "digits" that takes a positive integer n as input and returns the product of its odd digits and the sum of its even digits. If all digits are even, return the product of the first half of the even digits. If all digits are odd, return the sum of the first half of the odd digits. The function should handle edge cases.
"""

def digits(n):
    odd_digits, even_digits = [], []
    for i in str(n):
        if int(i) % 2 == 0:
            even_digits.append(int(i))
        else:
            odd_digits.append(int(i))
    
    product_odd = 1
    if odd_digits:
        for i in odd_digits:
            product_odd *= i

    sum_even = 0
    if even_digits:
        for i in even_digits:
            sum_even += i
    
    if even_digits and odd_digits:
        return sum_even + product_odd
    elif all([(int(i) % 2 == 0) for i in str(n)]):
        product = 1
        first_half = even_digits[:len(even_digits)//2]
        for i in first_half:
            product *= i
        return product
    else:
        first_half = odd_digits[:len(odd_digits)//2]
        return sum(first_half)