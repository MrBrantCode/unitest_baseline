"""
QUESTION:
Write a function `find_duplicates(arr)` that takes an array of integers `arr` as input and returns a list of duplicate elements in ascending order. The array size is limited to 1000 and the elements are in the range of -1000 to 1000. If there are no duplicates, return the string "No duplicates found." Do not modify the original array.
"""

def find_duplicates(arr):
    # Count the occurrences of each number
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    # Find the duplicate numbers
    duplicates = []
    for num in count:
        if count[num] > 1:
            duplicates.append(num)
    
    # Sort the duplicate numbers in ascending order
    duplicates.sort()
    
    # Return the result
    if len(duplicates) == 0:
        return "No duplicates found."
    else:
        return duplicates