"""
QUESTION:
Create a function called rearrange_numbers that takes a list of integers as input. Sort the list in descending order, then replace all even numbers with their binary equivalents as strings. Return the modified list.
"""

def rearrange_numbers(nums):
    """
    Sorts the input list of integers in descending order, 
    then replaces all even numbers with their binary equivalents as strings.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The modified list with even numbers replaced by their binary equivalents.
    """
    # Sorting the list in descending order.
    nums.sort(reverse=True)
    
    # Iterating over a copy of the sorted list.
    for i in nums[:]:
        # Checking if the number is even.
        if i % 2 == 0:
            # If the number is even, remove it from the list
            # and replace it with its binary equivalent.
            index = nums.index(i)
            nums.remove(i)
            nums.insert(index, bin(i)[2:])

    return nums