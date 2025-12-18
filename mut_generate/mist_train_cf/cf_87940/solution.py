"""
QUESTION:
Write a function `closest_pair(array, number)` to find the closest pair of numbers in the given array to the given number. The function should return the pair of numbers in the array that have a sum closest to the given number. If there are multiple pairs with the same minimum difference, the function should return the pair with the smallest product. The function must have at least 3 elements in the array; otherwise, it should return an error message.
"""

def closest_pair(array, number):
    if len(array) < 3:
        return "Error: Array must have at least 3 elements"

    closest_pair = []
    min_diff = float('inf')
    
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            diff = abs(array[i] + array[j] - number)
            
            if diff < min_diff:
                min_diff = diff
                closest_pair = [array[i], array[j]]
            elif diff == min_diff:
                product = array[i] * array[j]
                closest_product = closest_pair[0] * closest_pair[1]
                
                if product < closest_product:
                    closest_pair = [array[i], array[j]]
    
    return closest_pair