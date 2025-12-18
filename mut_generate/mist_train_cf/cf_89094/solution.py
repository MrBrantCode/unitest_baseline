"""
QUESTION:
Write a function called `fibonacci_multiplication` that takes in an integer `n`. The function should generate the first `n` numbers in a modified Fibonacci sequence, where each number is calculated by multiplying the two preceding numbers instead of adding them. The function should print the modified Fibonacci sequence, the sum of the sequence, and the product of the sequence. The function cannot use any built-in mathematical functions or operators for addition or multiplication, and must implement these operations from scratch.
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

    for num in sequence[:n]:
        print(num, end=', ')
    print()

    sum = calculate_sum(sequence[:n])
    product = calculate_product(sequence[:n])

    print(f"The sum is: {sum}")
    print(f"The product is: {product}")