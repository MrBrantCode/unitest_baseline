"""
QUESTION:
Write a function `fibonacci_between` that returns a list of Fibonacci numbers between the given low and high numbers (inclusive), where low is 1 and high is 100.
"""

def fibonacci_between(low, high):
    def fibonacci(limit):
        seq = [0, 1]
        while seq[-1] <= limit:
            seq.append(seq[-1] + seq[-2])
        return seq

    fibo_sequence = fibonacci(high)
    return [num for num in fibo_sequence if low <= num <= high]