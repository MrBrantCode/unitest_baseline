"""
QUESTION:
Implement a function named `unique_elements` that takes a list of numbers as input and returns a new list containing the unique elements from the original list, maintaining the original order of occurrence. The solution must have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.
"""

def unique_elements(nums):
    """
    Returns a new list containing the unique elements from the original list, 
    maintaining the original order of occurrence.

    Args:
    nums (list): A list of numbers.

    Returns:
    list: A new list containing the unique elements from the original list.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    # Create an empty dictionary to store the encountered elements
    encountered_nums = {}
    unique_nums = []

    # Iterate over each element in the list
    for num in nums:
        # Check if the element has already been encountered
        if num not in encountered_nums:
            # Add the element to the dictionary
            encountered_nums[num] = True
            # Append the element to the unique_nums list
            unique_nums.append(num)

    # Return the unique elements
    return unique_nums