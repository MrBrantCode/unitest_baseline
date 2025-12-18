"""
QUESTION:
Create a function `total_wait_time` that takes in the number of customers arriving per hour `A`, the average number of items in each customer's cart `I`, the time it takes to scan each item and process payment `S`, and the number of checkout lanes `L`. The function should return the total wait time for customers, calculated as `A * ((I * S) + ((A * I * S) / L))`. Using this function, find the optimal number of checkout lanes `L` that minimizes the total wait time. The input values for `A`, `I`, and `S` are given as 60, 10, and 0.5 respectively.
"""

def total_wait_time(A, I, S, L):
    return A * ((I * S) + ((A * I * S) / L))