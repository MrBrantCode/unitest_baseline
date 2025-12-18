"""
QUESTION:
Write a function `find_highest_product(arr)` that finds the pair of numbers in the given array `arr` with the highest product, considering all possible combinations. If there are multiple pairs with the same highest product, return the pair with the smallest absolute sum. If there are no pairs in the array, return `None`. The function should have a time complexity of O(n^2), where n is the length of the input array.
"""

def find_highest_product(arr):
    max_product = float('-inf')
    max_pair = None
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                max_pair = (arr[i], arr[j])
            elif product == max_product:
                if abs(arr[i] + arr[j]) < abs(max_pair[0] + max_pair[1]):
                    max_pair = (arr[i], arr[j])
    
    if max_pair is None:
        return None
    return max_pair