"""
QUESTION:
Write a function named `min_product` that takes an array of integers as input and returns the pair, triple, quadruple, and quintuple of integers with the minimum product. The function should handle arrays with less than five integers and consider cases with both positive and negative numbers, including zeroes. The time complexity should be better than O(n^5).
"""

def min_product(arr):
    arr.sort()

    if len(arr) < 5:
        return "Array has fewer than 5 elements. Can't find quintuple."
    
    pair = (arr[0], arr[1])
    triple = (arr[0], arr[1], arr[2])
    quadruple = (arr[0], arr[1], arr[2], arr[3])
    quintuple = (arr[0], arr[1], arr[2], arr[3], arr[4])
    
    return pair, triple, quadruple, quintuple