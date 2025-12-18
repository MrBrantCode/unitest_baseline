"""
QUESTION:
Create a function named `isMonotonic` that determines whether a given array of integers is strictly monotonically increasing or decreasing. The function should return `True` if the array is strictly increasing or decreasing, and `False` otherwise. The function should consider arrays with duplicate numbers as not strictly increasing or decreasing. Optimize the function for time and space complexity.
"""

def isMonotonic(A):
    return (all(A[i] < A[i+1] for i in range(len(A) - 1)) or
            all(A[i] > A[i+1] for i in range(len(A) - 1)))