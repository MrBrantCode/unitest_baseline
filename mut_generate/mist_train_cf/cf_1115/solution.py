"""
QUESTION:
Write a function `find_pairs(arr, target)` that takes an array of integers and a target number as input, and returns a list of unique pairs of numbers from the array whose product is equal to the target number. The function should have a time complexity of O(nlogn) or better, and should not use additional space beyond the output array for storing the pairs. The output list should contain unique pairs in non-decreasing order, with no duplicate pairs.
"""

def find_pairs(arr, target):
    """
    Find unique pairs of numbers from the array whose product is equal to the target number.

    Args:
        arr (list): A list of integers.
        target (int): The target number.

    Returns:
        list: A list of unique pairs of numbers from the array whose product is equal to the target number.

    """
    seen = set()
    pairs = set()  # Using set to store unique pairs
    
    for num in arr:
        if num != 0 and target % num == 0 and target // num in seen:
            # Store pairs in a sorted order
            pairs.add(tuple(sorted((num, target // num))))
        seen.add(num)
    
    # Convert the set of pairs to a list and sort it
    pairs = sorted(list(pairs), key=lambda x: x[0])
    
    return pairs