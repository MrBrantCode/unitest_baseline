"""
QUESTION:
Design a function `fibonacci_square_sum` that generates a Fibonacci sequence up to `n` elements, calculates the square of each element, and inserts these squared values into a new array in ascending order. The function should also return the sum of the elements in the sorted array. The time complexity of the function should be O(n log n). The input `n` is a positive integer representing the number of elements in the Fibonacci sequence.
"""

import bisect

def fibonacci_square_sum(n):
    fibonacci = [0, 1]
    squares = [0, 1]
    total = 1
    for _ in range(2, n):
        next_fibonacci = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_fibonacci)
        square = next_fibonacci ** 2
        total += square
        bisect.insort(squares, square)
    return squares, total