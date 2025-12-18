"""
QUESTION:
Write a function called `getFibonacciNumbers` that takes an integer `numTerms` as input and returns the first `numTerms` numbers in the Fibonacci sequence. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
"""

def getFibonacciNumbers(numTerms):
    sequence = [0, 1]
    while len(sequence) < numTerms:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:numTerms]