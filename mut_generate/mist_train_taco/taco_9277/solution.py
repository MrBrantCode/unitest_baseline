"""
QUESTION:
The "Russian Peasant Method" is an old algorithm used by Russian peasants (and before them ancient Egyptians) to perform multiplication.  Consider that X and Y are two numbers.  X can be any number but Y must be a positive integer. To multiply X and Y:

1. Let the product = 0
2. If Y is odd, then the product = product + X
3. X = X + X
4. Y = integer part of Y / 2 
5. if Y is nonzero, repeat from step 2; otherwise the algorithm terminates and returns the product.

For example:

Let X = 10

Let Y = 5

X: 10 20 40 80

Y: 5  2  1  0

product = 10 + 40 = 50

Note: usage of multiplication is of course forbidden...
"""

def russian_peasant_multiplication(x, y):
    """
    Multiplies two numbers using the Russian Peasant Method.

    Parameters:
    x (int or float): The first number.
    y (int): The second number, which must be a positive integer.

    Returns:
    int or float: The product of x and y.
    """
    product = 0
    while y != 0:
        if y % 2 == 1:
            product += x
        x += x
        y //= 2
    return product