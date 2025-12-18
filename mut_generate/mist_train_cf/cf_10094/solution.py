"""
QUESTION:
Create a function `find_duplicates(nums)` that takes an array of numbers as input, where the length of the array does not exceed 1000. The function should return a list of indices of all duplicate values found in the array.
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