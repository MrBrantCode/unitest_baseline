"""
QUESTION:
Design a function `solve_problem(n)` that generates a multi-dimensional matrix of size `n x n` filled with the first `n*n` prime numbers and prints the numbers in a spiral order starting from the top left corner in a counterclockwise direction. The function should not take any input other than `n`, and should not use any external libraries or pre-computed lists of prime numbers.
"""

def solve_problem(n):
    def prime_generator():
        yield 2
        primes = [2]
        num = 3
        while True:
            if all(num % prime != 0 for prime in primes):
                primes.append(num)
                yield num
            num += 2

    def generate_matrix(n, primes):
        matrix = [[0]*n for _ in range(n)]
        for i in range(n*n):
            row, col = divmod(i, n)
            matrix[row][col] = next(primes)
        return matrix

    def print_spiral(matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result += [row.pop()]
            if matrix:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result += [row.pop(0)]
        return result

    primes = prime_generator()
    matrix = generate_matrix(n, primes)
    return print_spiral(matrix)