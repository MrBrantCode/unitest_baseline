"""
QUESTION:
Write a function named `get_factorial` that takes a positive integer `n` as input and returns the factorial of `n`. Using this function, compute the multiplication of the factorials of all the odd integers within the range from 1 to `n` inclusive, calculate its modulus `m`, and print the result. The inputs `n` and `m` are two positive integers provided by the user.
"""

def entrance(n, m):
    def get_factorial(k):
        if k == 1 or k == 0:
            return 1
        else:
            return k * get_factorial(k - 1)

    mult = 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            mult *= get_factorial(i)
    return mult % m