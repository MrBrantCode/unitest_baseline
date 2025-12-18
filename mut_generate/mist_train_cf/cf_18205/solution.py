"""
QUESTION:
Write a function `find_closest_pair` that takes an array of numbers and a target number as input, and returns the closest pair of numbers in the array to the target number. The array should have at least 2 elements. If the target number is not present in the array, return the closest pair of numbers in the array. If there are multiple pairs of numbers equally close to the target number, return the pair with the smallest sum.
"""

def find_closest_pair(arr, num):
    if len(arr) < 2:
        return "Error: Array should have at least 2 elements"
    
    arr.sort()  # Sort the array in ascending order
    closest_pair = (arr[0], arr[1])  # Initialize the closest pair with first two elements
    
    # Iterate through the array to find the closest pair
    for i in range(len(arr)-1):
        curr_pair = (arr[i], arr[i+1])
        
        # If the given number is between the pair, return the pair
        if arr[i] <= num <= arr[i+1]:
            return curr_pair
        
        # If the pair is closer to the given number than the current closest pair
        if abs(sum(curr_pair) - num) < abs(sum(closest_pair) - num):
            closest_pair = curr_pair
    
    return closest_pair