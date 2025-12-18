"""
QUESTION:
Create a function named `additive_multiplicative` that takes an integer `num` as input and returns a tuple containing the sum and product of its digits. The function should handle both positive and negative integers, ignoring the negative sign when calculating the sum and product. The function should also handle zeros by only contributing them to the sum and not the product.
"""

def additive_multiplicative(num):
    total_sum = 0
    product = 1
    for i, digit in enumerate(str(abs(num))):
        total_sum += int(digit)
        if int(digit) != 0:    
            product *= int(digit)
    return (total_sum, product)