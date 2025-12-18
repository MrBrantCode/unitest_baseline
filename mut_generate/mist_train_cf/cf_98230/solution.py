"""
QUESTION:
Create a function named "subtract_vectors" that takes two input vectors x and y of equal lengths. The function should initialize a new vector called "result" by subtracting each corresponding element of y from x and return the resultant vector.
"""

def subtract_vectors(x, y):
    result = []
    for i in range(len(x)):
        result.append(x[i]-y[i])
    return result