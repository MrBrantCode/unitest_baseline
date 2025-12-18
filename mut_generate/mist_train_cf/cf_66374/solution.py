"""
QUESTION:
Design a function called `lucas_sequence_analysis` that takes an integer `N` as input. This function should analyze the first `N` numbers in the Lucas sequence and return the number of Perfect numbers, the number of Fibonacci divisors, and their respective indices (starting from 0) in the sequence. A Perfect number is a positive integer that is equal to the sum of its proper positive divisors excluding the number itself. A Fibonacci divisor refers to numbers in the Lucas sequence that are also in the Fibonacci sequence. The Lucas sequence starts as 2, 1, 3, 4, 7, ... and each number is the sum of its two immediate predecessors.
"""

def lucas_sequence_analysis(N):
    def is_fibonacci(n):
        a, b = 0, 1
        while a < n:
            a, b = b, a+b
        return n == a

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif i * (n // i) == n:
                sum = sum + i + n//i
                i += 1
        return sum == n and n!=1

    lucas = [2, 1]
    for i in range(2, N):
        lucas.append(lucas[-1] + lucas[-2])

    perfect_numbers = [(i, num) for i, num in enumerate(lucas) if is_perfect(num)]
    fibonacci_numbers = [(i, num) for i, num in enumerate(lucas) if is_fibonacci(num)]

    return len(perfect_numbers), len(fibonacci_numbers), perfect_numbers, fibonacci_numbers