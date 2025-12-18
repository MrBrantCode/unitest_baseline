"""
QUESTION:
Create a function called `fibonacci` that generates a Fibonacci sequence iteratively with a time complexity of O(n) and a space complexity of O(1), where n is the desired length of the sequence. The function should not use recursion, mathematical operations for generating the sequence (addition or multiplication), or any external libraries. The function should return a list of the first n numbers in the Fibonacci sequence.
"""

def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0, 1]

    for i in range(2, n):
        current = sequence[i-1] + sequence[i-2]
        sequence.append(current)

    return sequence[:n]