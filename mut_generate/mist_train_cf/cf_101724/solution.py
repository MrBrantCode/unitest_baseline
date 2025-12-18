"""
QUESTION:
Write a function `calculate_difference` that takes three integers as input and returns the difference between the product of their sum and the quotient of the first two integers, and the product of their sum and the quotient of a predefined constant and the third integer. The function should also display the values of each variable used in the calculation in a table. The predefined constants are 98765 for the first quotient and 5436 for the second quotient.
"""

def calculate_difference(a, b, c):
    """
    Calculate the difference between the product of the sum of three integers and the quotient of the first two integers,
    and the product of their sum and the quotient of a predefined constant and the third integer.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.

    Returns:
        float: The difference between the two products.
    """
    sum_abc = a + b + c
    product1 = sum_abc * (98765 / a)
    product2 = sum_abc * (5436 / c)
    diff = product1 - product2

    # display the result in a table
    print("| Variable | Value |")
    print("|----------|---------|")
    print(f"| a | {a} |")
    print(f"| b | {b} |")
    print(f"| c | {c} |")
    print(f"| sum_abc | {sum_abc} |")
    print(f"| product1 | {product1:.2f} |")
    print(f"| product2 | {product2:.2f} |")
    print(f"| diff | {diff:.2f} |")
    return diff