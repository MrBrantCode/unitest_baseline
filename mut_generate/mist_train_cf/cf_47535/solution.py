"""
QUESTION:
Create a function named `sum_of_products` that takes a list of integers as input and returns the sum of the products of every conceivable sublist within the specified list. The function should have a time complexity of O(n) to efficiently handle large lists.
"""

def sum_of_products(arr):
    result = 0
    n = len(arr)
    
    for i in range(n):
        result += (arr[i] * (i+1) * (n-i))
        
    return result