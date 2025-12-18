"""
QUESTION:
Write a function `remove_duplicates(arr)` that takes an array of integers `arr` and returns an array of all elements in `arr` except for the duplicates. The function should have a time complexity of O(n), where n is the length of the array, and should not use any built-in functions or libraries to achieve this task.
"""

def remove_duplicates(arr):
    # Create an empty dictionary to track the count of each number
    count_dict = {}
    
    # Iterate through the array
    for num in arr:
        # If the number is already in the dictionary, increase its count
        if num in count_dict:
            count_dict[num] += 1
        # Otherwise, add the number to the dictionary with count 1
        else:
            count_dict[num] = 1
    
    # Create an empty list to store the result
    result = []
    
    # Iterate through the array again
    for num in arr:
        # If the count of the number is 1, add it to the result
        if count_dict[num] == 1:
            result.append(num)
    
    # Return the result array
    return result