"""
QUESTION:
You are given an equation: 

Ax2 + Bx + C = 0. 

Your task is to find the number of distinct roots of the equation and print all of them in ascending order.

Input

The first line contains three integer numbers A, B and C ( - 105 ≤ A, B, C ≤ 105). Any coefficient may be equal to 0.

Output

In case of infinite root count print the only integer -1. In case of no roots print the only integer 0. In other cases print the number of root on the first line and the roots on the following lines in the ascending order. Print roots with at least 5 digits after the decimal point.

Examples

Input

1 -5 6


Output

2
2.0000000000
3.0000000000
"""

def solve_quadratic_equation(a, b, c):
    # Calculate the discriminant
    D = b ** 2 - 4 * a * c
    
    # Handle special cases
    if a == 0 and b == 0 and c != 0:
        return 0, []
    elif a == 0 and b == 0 and c == 0:
        return -1, []
    elif a == 0:
        x0 = -c / b
        return 1, [round(x0, 5)]
    elif b == 0:
        if -c / a >= 0:
            x0 = (-c / a) ** 0.5
            return 1, [round(x0, 5)]
        else:
            return 0, []
    elif D < 0:
        return 0, []
    elif D == 0:
        x = -b / (2 * a)
        return 1, [round(x, 5)]
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        roots = sorted([round(x1, 5), round(x2, 5)])
        return 2, roots