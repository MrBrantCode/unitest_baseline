"""
QUESTION:
Create a function named `fibLucas(n)` that generates the first `n` elements of the Fibonacci sequence and the Lucas sequence. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. The Lucas sequence starts with 2 and 1, and also follows the same principle. The function should be able to handle values of `n` up to a maximum of 10000.
"""

def fibLucas(n):
    if n>10000:
        return 'Input exceeds limit, please enter a number up to a maximum of 10000'

    # initialize fibonacci sequence
    fibSequence = [0, 1]
    for i in range(2, n):
        nextVal = fibSequence[i-1] + fibSequence[i-2]
        fibSequence.append(nextVal)

    # initialize lucas sequence
    lucasSequence = [2, 1]
    for i in range(2, n):
        nextVal = lucasSequence[i-1] + lucasSequence[i-2]
        lucasSequence.append(nextVal)
    return fibSequence[:n], lucasSequence[:n]