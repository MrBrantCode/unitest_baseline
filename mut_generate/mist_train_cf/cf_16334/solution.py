"""
QUESTION:
Create a function named 'find_unique_elements' that takes an array of integers as input and returns a list of all the elements that appear exactly once in the array. The function should return the elements in the order of their first occurrence in the input array. The input array can be empty, contain both positive and negative numbers, and zero, and repeated negative numbers should only be considered as duplicates if they occur consecutively.
"""

def find_unique_elements(arr):
    # Step 1: Create a dictionary to count the occurrences of each element
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Step 2: Create a list to store the unique elements
    unique_elements = []
    
    # Step 3: Iterate over the original array to maintain order of first occurrence
    for num in arr:
        if counts[num] == 1:
            unique_elements.append(num)
            # Set the count of the current element to a negative value
            # to avoid adding it again if it appears later in the array
            counts[num] = -1
    
    # Step 4: Return the unique_elements list
    return unique_elements