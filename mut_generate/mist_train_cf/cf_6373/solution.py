"""
QUESTION:
Write a function `find_duplicate_numbers` that takes an array of integers as input, finds the duplicate numbers in the array, and returns them in ascending order. The array size is limited to 1000 elements, and the elements are in the range of -1000 to 1000. If there are no duplicates, return "No duplicates found." The function should not modify the original array.
"""

def find_duplicate_numbers(nums):
    # Create a hashmap to count occurrences
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    # Create a result array for duplicate numbers
    duplicates = []
    for num, freq in count.items():
        if freq > 1:
            duplicates.append(num)
    
    # Sort the result array in ascending order
    duplicates.sort()
    
    # If no duplicates found, return "No duplicates found."
    if len(duplicates) == 0:
        return "No duplicates found."
    
    return duplicates