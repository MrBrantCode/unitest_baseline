"""
QUESTION:
Develop a function named `sum_of_digits` that takes two integer inputs `a` and `b` of varying length and returns the sum of all individual digits across both numbers. The function should work for any positive integer inputs. The function should calculate the sum of digits of `a` and `b` separately and then return the total sum.
"""

def sum_of_digits(a, b):
    # Converting numbers to strings and then to list of characters
    a_digits = list(str(a))
    b_digits = list(str(b))
    
    # Converting individual characters back to integers
    a_digits = [int(i) for i in a_digits]
    b_digits = [int(i) for i in b_digits]

    # Adding the sum of digits of a and sum of digits of b
    return sum(a_digits) + sum(b_digits)