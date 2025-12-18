"""
QUESTION:
Create a function `h` that takes two integers `n` and `m` as inputs. The function should return a list of `m` elements, where each element at index `i` (starting from 0) is calculated based on the number `n + i`. If `n + i` is even, the element is the sum of all even numbers from 1 to `n + i`. If `n + i` is odd, the element is the product of all even numbers from 1 to `n + i`.
"""

def h(n, m):
    def sum_even_numbers(num):
        return sum(x for x in range(2, num + 1) if x % 2 == 0)

    def product_even_numbers(num):
        product = 1
        for y in range(2, num + 1):
            if y % 2 == 0:
                product *= y
        return product

    return [sum_even_numbers(n + i) if (n + i) % 2 == 0 else product_even_numbers(n + i) for i in range(m)]