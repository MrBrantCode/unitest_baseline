"""
QUESTION:
Design a function named `conjugate_products` that takes an array of complex numbers as input and returns an array of all possible conjugate products of two different complex numbers. The function should not duplicate the same pair of complex numbers and should have a time complexity of O(n^2) or less.
"""

def conjugate_products(arr):
    n = len(arr)
    if n <= 1: 
        return []
    else:  
        products = []
        for i in range(n):
            for j in range(i+1, n):  
                product = arr[i]*arr[j].conjugate()  
                products.append(product)
        return products