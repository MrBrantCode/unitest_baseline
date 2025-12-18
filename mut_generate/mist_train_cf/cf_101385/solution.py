"""
QUESTION:
Write a function named `calculate_difference` that takes three integers `a`, `b`, and `c` as input and returns the difference between the product of the sum of `a`, `b`, and `c` and the quotient of `b` and `a`, and the product of the sum of `a`, `b`, and `c` and the quotient of `5436` and `15678`. The function should also print a table showing the values of each variable used in the calculation. The function should round the product values to two decimal places.
"""

def calculate_difference(a, b, c):
    # calculate the sum of the three integers
    sum_abc = a + b + c
    # calculate the difference between two products
    product1 = sum_abc * (b / a)
    product2 = sum_abc * (5436 / 15678)
    diff = product1 - product2
    
    # display the result in a table
    print("| Variable | Value   |")
    print("|----------|---------|")
    print(f"| a        | {a}    |")
    print(f"| b        | {b}    |")
    print(f"| c        | {c}    |")
    print(f"| sum_abc  | {sum_abc} |")
    print(f"| product1 | {product1:.2f} |")
    print(f"| product2 | {product2:.2f} |")
    print(f"| diff     | {diff:.2f} |")
    return diff