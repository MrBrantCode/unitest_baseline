"""
QUESTION:
Develop a function `productFib(M, N, P)` that calculates the product of all Fibonacci numbers between N and M inclusively that are greater than P. The function should generate Fibonacci numbers up to M, handle cases where N is greater than M, and handle cases where P is larger than all Fibonacci numbers within the M range.
"""

def productFib(M, N, P):
    # Check if N is greater than M
    if N > M:
        return "Invalid Input: N should be less than or equal to M"

    # Start Fibonacci series
    fib = [0, 1]
    while fib[-1] <= M:
        fib.append(fib[-1] + fib[-2])

    # Handle case where P is larger than all Fibonacci numbers
    if P >= fib[-1]:
        return "Invalid Input: P is larger than all Fibonacci numbers within the M range"

    # Compute product of Fibonacci numbers between N and M that are greater than P
    product = 1
    for num in fib:
        if N <= num <= M and num > P:
            product *= num

    return product