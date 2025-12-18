"""
QUESTION:
Write a function `find_largest_sum(arr)` that finds the two elements in an array of positive integers with the largest sum. The function should return these two elements. 

The array can contain duplicates and may not be sorted. If there are multiple pairs with the same maximum sum, any pair can be returned. The function should have a time complexity of O(n) and a space complexity of O(1), and it should not use any built-in sorting functions.
"""

def find_largest_sum(arr):
    largest_elements = [float('-inf'), float('-inf')]  
    max_sum = float('-inf')  

    for num in arr:
        if num > largest_elements[0]:  
            largest_elements[1] = largest_elements[0]
            largest_elements[0] = num
        elif num > largest_elements[1]:  
            largest_elements[1] = num
        
        if num + largest_elements[1] > max_sum:  
            max_sum = num + largest_elements[1]
    
    return largest_elements