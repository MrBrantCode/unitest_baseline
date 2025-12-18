"""
QUESTION:
Create a function called `total_wait_time` that calculates the total wait time for customers given the number of customers arriving per hour, the average number of items in each customer's cart, the time it takes to scan each item and process payment, and the number of checkout lanes. The total wait time can be calculated as A * [(I * S) + ((A * I * S) / L)], where A is the number of customers arriving per hour, I is the average number of items in each customer's cart, S is the time to scan and process payment, and L is the number of checkout lanes. The function should return the total wait time. 

The function should not take any additional arguments other than the number of customers arriving per hour, the average number of items in each customer's cart, the time it takes to scan each item and process payment, and the number of checkout lanes. 

You can assume that the input values will be positive numbers.
"""

def total_wait_time(A, I, S, L):
    return A * ((I * S) + ((A * I * S) / L))