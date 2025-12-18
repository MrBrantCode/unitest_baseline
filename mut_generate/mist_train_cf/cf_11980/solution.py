"""
QUESTION:
Create a function called `subset_with_threshold` that takes two parameters: an array `arr` of integers and a positive integer `threshold`. The function should return a subset of `arr` containing unique elements with lengths of their string representation less than the given `threshold`, sorted in ascending order.
"""

def subset_with_threshold(arr, threshold):
    # Filter the array to keep only the elements with length smaller than the threshold
    filtered = [x for x in arr if len(str(x)) < threshold]
    
    # Remove duplicates and sort the filtered array in ascending order
    sorted_filtered = sorted(list(set(filtered)))
    
    return sorted_filtered