"""
QUESTION:
Implement a function `get_third_largest` that takes a sequence as input, removes duplicates, and returns the third largest unique element. If the sequence has less than three unique elements, the function should return `None`. The function must achieve this in a time complexity of O(n) without using built-in sorting functions or libraries.
"""

def get_third_largest(seq):
    # Remove duplicates from the sequence
    unique_seq = list(set(seq))

    # If the length of the unique sequence is less than 3, return None
    if len(unique_seq) < 3:
        return None

    # Initialize the three largest variables
    largest = float('-inf')
    second_largest = float('-inf')
    third_largest = float('-inf')

    # Find the three largest elements in the sequence
    for num in unique_seq:
        if num > largest:
            third_largest = second_largest
            second_largest = largest
            largest = num
        elif num > second_largest:
            third_largest = second_largest
            second_largest = num
        elif num > third_largest:
            third_largest = num

    return third_largest