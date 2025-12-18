"""
QUESTION:
Implement the `multiply_list` function to calculate the product of all elements in a list of integers. The function should not use the '*' operator or any built-in multiplication functions. Instead, it should utilize addition, subtraction, bit shifting operations, and bitwise logic operators. The function should handle lists containing both positive and negative integers and achieve a time complexity of O(n), where n is the length of the list.
"""

def multiply_list(lst):
    def multiply(a, b):
        res = 0
        while b:
            if b & 1:
                res += a
            a <<= 1
            b >>= 1
        return res

    def divide(a, b):
        res = 0
        while a >= b:
            shift = 0
            while (b << shift) <= a:
                shift += 1
            res += (1 << (shift - 1))
            a -= (b << (shift - 1))
        return res

    def pow(b, p):
        res = 1
        while p:
            if p & 1:
                res = multiply(res, b)
            b = multiply(b, b)
            p >>= 1
        return res

    product = 1
    for num in lst:
        if num == 0:
            return 0
        if num < 0:
            product = -product
            num = -num
        factors = 0
        while num % 2 == 0:
            num >>= 1
            factors += 1
        product = multiply(product, pow(2, factors))
        product = multiply(product, num)
    return product