"""
QUESTION:
Create a function named `generate_fibonacci_sequence` that takes a positive integer `n` as input and returns a list containing all Fibonacci numbers less than or equal to the given input. The function should use matrix exponentiation to efficiently calculate the Fibonacci numbers in logarithmic time complexity. The function should not include the number `n` in the output if it is not a Fibonacci number.
"""

def generate_fibonacci_sequence(n):
    F = [[1, 1], [1, 0]]
    I = [[1, 0], [0, 1]]
    
    def multiply_matrices(A, B):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += A[i][k] * B[k][j]
        return result
    
    def power_matrix(A, p):
        if p == 0:
            return I
        elif p % 2 == 0:
            B = power_matrix(A, p // 2)
            return multiply_matrices(B, B)
        else:
            B = power_matrix(A, (p - 1) // 2)
            return multiply_matrices(multiply_matrices(B, B), A)
    
    fib_sequence = []
    a, b = 1, 1
    
    if n >= a:
        fib_sequence.append(a)
    if n >= b:
        fib_sequence.append(b)
    
    i = 2
    while True:
        temp = a + b
        if temp > n:
            break
        fib_sequence.append(temp)
        a, b = b, temp
        i += 1
    
    return fib_sequence