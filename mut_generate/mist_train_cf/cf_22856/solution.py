"""
QUESTION:
Write a function `find_highest_product_pair` that takes an array of numbers as input and returns the pair of numbers with the highest product. If there are multiple pairs with the same highest product, return the pair with the smallest absolute sum. If there are no pairs in the array, return None. The function should have a time complexity of O(n^2), where n is the length of the input array.
"""

def find_highest_product_pair(numbers):
    if len(numbers) < 2:
        return None
    
    highest_product = float('-inf')
    highest_product_pair = None
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            product = numbers[i] * numbers[j]
            if product > highest_product:
                highest_product = product
                highest_product_pair = (numbers[i], numbers[j])
            elif product == highest_product:
                if abs(numbers[i] + numbers[j]) < abs(sum(highest_product_pair)):
                    highest_product_pair = (numbers[i], numbers[j])
    
    return highest_product_pair