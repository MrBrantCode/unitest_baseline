"""
QUESTION:
The solution of $ x ^ 3 = q $ is to calculate the recurrence formula $ x_ {n + 1} = x_n-\ frac {x_ {n} ^ 3 --q} {3x_ {n} ^ 2} $ It can be calculated approximately with.

Put a positive number $ \ frac {q} {2} $ in $ x_1 $

$ x_2 = x_1-\ frac {x_ {1} ^ 3 --q} {3x_ {1} ^ 2} $, $ x_3 = x_2-\ frac {x_ {2} ^ 3 --q} {3x_ {2} ^ Calculate as 2} $,….

While doing this calculation

When the value of $ | x ^ 3 --q | $ becomes small enough, stop the calculation and use the last calculated $ x_n $ as an approximate solution of $ x ^ 3 = q $.

Follow this method to create a program that outputs an approximation of the cube root of $ q $ for the input positive integer $ q $. However, use $ | x ^ 3-q | <0.00001 q $ to determine that it is "small enough".



input

Multiple datasets are given. For each dataset, $ q $ ($ 1 \ leq q <2 ^ {31} $) (integer) is given on one line. The end of the input is -1.

The number of datasets does not exceed 50.

output

Print $ x $ (real number) on one line for each dataset. The output result may contain an error of 0.00001 or less.

Example

Input

15
15
-1


Output

2.466212
2.466212
"""

def approximate_cube_root(q: int, tolerance: float = 1e-05) -> float:
    """
    Approximates the cube root of a given integer `q` using a recurrence formula.

    Parameters:
    - q (int): The integer for which the cube root is to be approximated.
    - tolerance (float): The tolerance level for the approximation (default is 1e-05).

    Returns:
    - float: The approximate cube root of `q`.
    """
    x = q / 2
    while abs(x ** 3 - q) >= tolerance * q:
        x -= (x ** 3 - q) / (3 * x ** 2)
    return x