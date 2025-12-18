"""
QUESTION:
Create a function `g` that takes an integer `n` as input and returns a list of `n` elements. For each index `i` in the list, if `i` is even, the element should be the sum of all even numbers up to `i`. If `i` is odd, the element should be the product of all even numbers from 1 to `i`.
"""

def g(n):
    def even_product(i):
        product = 1
        for num in range(2, i+1, 2):
            product *= num
        return product

    def even_sum(i):
        s = 0
        for num in range(2, i+1, 2):
            s += num
        return s

    output = []

    for i in range(1, n+1):
        if i % 2 == 0:
            output.append(even_sum(i))
        else:
            output.append(even_product(i))

    return output