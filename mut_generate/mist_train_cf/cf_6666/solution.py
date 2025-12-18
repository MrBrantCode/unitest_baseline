"""
QUESTION:
Generate a function named `fibonacci_sequence` that takes an integer `n` as input, and returns a list of Fibonacci numbers up to `n`. The function should use a closed-form expression (also known as Binet's formula) to calculate the Fibonacci numbers without using recursion or loops. Additionally, calculate the sum of the even numbers in the sequence and the product of the odd numbers.
"""

import math

def fibonacci_sequence(n):
    phi = (1 + math.sqrt(5)) / 2
    sequence = []
    i = 0
    while True:
        fib_num = int((math.pow(phi, i) - math.pow(-phi, -i)) / math.sqrt(5))
        if fib_num > n:
            break
        sequence.append(fib_num)
        i += 1
    
    even_sum = sum(num for num in sequence if num % 2 == 0)
    odd_product = 1
    for num in sequence:
        if num % 2 != 0:
            odd_product *= num

    return sequence, even_sum, odd_product