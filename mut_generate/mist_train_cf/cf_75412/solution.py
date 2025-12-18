"""
QUESTION:
Write a function to calculate the outcome of recursively applying functions f and g to an initial value x 8 times each, alternating between the two functions, where f(x) = (1+x) / (1-x) and g(x) = -2 / (x+1). The initial value x is 12. Implement this in Python.
"""

def entrance(x):
    def recursive_f(x):
        return (1+x) / (1-x)

    def recursive_g(x):
        return -2 / (x+1)

    for _ in range(8):
        x = recursive_g(recursive_f(x))
    return x