"""
QUESTION:
Write a function named `fibonacci_multiplication` that takes an integer `n` as input, generates the first `n` numbers in a modified Fibonacci sequence where each term is the product of the two preceding terms (instead of their sum), and calculates the sum and product of the generated sequence. The function should implement multiplication and addition operations from scratch without using any built-in mathematical functions or operators for addition or multiplication.
"""

def fibonacci_multiplication(n):
    def multiply(a, b):
        if a == 0 or b == 0:
            return 0

        sign = 1 if (a > 0 and b > 0) or (a < 0 and b < 0) else -1

        a = abs(a)
        b = abs(b)
        result = 0

        for _ in range(b):
            result += a

        return result * sign

    def add(a, b):
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a

    def calculate_sum(sequence):
        sum = 0
        for num in sequence:
            sum = add(sum, num)
        return sum

    def calculate_product(sequence):
        product = 1
        for num in sequence:
            product = multiply(product, num)
        return product

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(multiply(sequence[i-1], sequence[i-2]))

    sum = calculate_sum(sequence[:n])
    product = calculate_product(sequence[:n])

    return sum, product