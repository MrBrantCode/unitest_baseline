"""
QUESTION:
Create a function named `find_duplicates(nums)` that takes a list of numbers `nums` as input and returns a list of indices where duplicate values are found. The input list will have a length of at most 1000 and may contain duplicate values; the function should return the indices of all occurrences of these duplicates.
"""

def find_duplicates(nums):
    # Create a dictionary to store the count of each number
    count = {}
    # Create a list to store the indices of duplicate values
    duplicates = []
    
    # Iterate through the input array
    for i, num in enumerate(nums):
        # If the number is already in the dictionary, it's a duplicate
        if num in count:
            # Add the index of the duplicate value to the list
            duplicates.append(i)
        # Increment the count of the number in the dictionary
        count[num] = count.get(num, 0) + 1
    
    # Return the list of duplicate indices
    return duplicates