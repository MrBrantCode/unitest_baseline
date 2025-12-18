"""
QUESTION:
Create a function `modified_fibonacci(n)` that generates a sequence similar to the Fibonacci sequence, but with alternating starting values of 0 and 1, and returns the sequence of length `n`. The sequence should follow the Fibonacci rule of adding the last two numbers to generate the next number, with the exception of the starting values which alternate between 0 and 1.
"""

def modified_fibonacci(n):
    results = []
    for i in range(n):
        if i%2 == 0:
            if i >= 2:
                results.append(results[-1] + results[-2])
            else:
                results.append(0)
        else:
            if i == 1:
                results.append(1)
            else:
                results.append(results[-1] + results[-2])
                 
    return results