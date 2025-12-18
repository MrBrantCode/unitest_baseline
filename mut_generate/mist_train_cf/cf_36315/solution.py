"""
QUESTION:
Implement the `getMultiplier` function that takes two integer arguments and returns a multiplier based on the following rules: 
- If the two integers are equal, the multiplier should be 1.
- If the two integers are different, the multiplier should be 0.
Implement the function in a way to optimize the code snippet to efficiently process a signal, which is a list of integers. The optimized code should calculate a new signal by multiplying each element of the signal list with a corresponding multiplier obtained from the `getMultiplier` function and then summing the results.
"""

def getMultiplier(i, j):
    return 1 if i == j else 0