"""
QUESTION:
Design a function named `conjugate_product` that takes two complex numbers `num1` and `num2` as input and returns the product of their conjugates. The function should utilize Python's built-in support for complex numbers.
"""

def conjugate_product(num1, num2):
    # calculate the conjugates of the complex numbers
    num1_conjugate = num1.conjugate()
    num2_conjugate = num2.conjugate()

    # return the product of the conjugates
    return num1_conjugate * num2_conjugate