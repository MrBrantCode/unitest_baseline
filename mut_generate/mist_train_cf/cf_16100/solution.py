"""
QUESTION:
Implement a function called `group_numbers` that groups a list of numbers into sublists of four consecutive numbers. The grouping should start from the third element in the list. If the list has fewer than three elements, return an empty list. If the remaining elements are not enough to form a full group of four, they should be included in the last group.
"""

def group_numbers(nums):
    """
    Group a list of numbers into sublists of four consecutive numbers.
    
    Args:
    nums (list): A list of numbers.
    
    Returns:
    list: A list of sublists of four consecutive numbers.
    """
    # Check if the list has fewer than three elements
    if len(nums) < 3:
        return []
    
    # Grouping into groups of four starting from the third element
    return [nums[i:i+4] for i in range(2, len(nums), 4)]