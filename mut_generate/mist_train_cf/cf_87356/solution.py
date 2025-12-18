"""
QUESTION:
Calculate the median of an array of integers without using any built-in functions or libraries that directly calculate the median. The median should be accurate up to 2 decimal places. Implement a function named `calculate_median()` that takes an array of integers as input and returns the median. The function should handle edge cases such as empty arrays or arrays containing only negative numbers.
"""

def calculate_median(arr):
    # Step 1: Sort the array in ascending order
    arr = sorted(arr)

    # Step 2: Determine the length of the sorted array
    length = len(arr)

    # Step 3: Calculate the median for odd length array
    if length % 2 == 1:
        median = arr[(length - 1) // 2]
    
    # Step 4: Calculate the median for even length array
    else:
        mid1 = arr[length // 2]
        mid2 = arr[(length // 2) - 1]
        median = (mid1 + mid2) / 2
    
    # Step 5: Round the median to a certain decimal place (e.g., 2 decimal places)
    median = round(median, 2)
    
    return median