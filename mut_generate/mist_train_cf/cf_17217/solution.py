"""
QUESTION:
Create a recursive function named `recursive_sum` that takes a list of numbers as input and returns the sum of the elements that are divisible by 3 and greater than or equal to 10, along with the count of such elements. The function should not use any loops and must utilize recursion to traverse the list.
"""

def recursive_sum(lst, total_sum=0, count=0):
    """
    Recursively calculates the sum of elements divisible by 3 and greater than or equal to 10,
    along with their count.

    Args:
    lst (list): A list of numbers.
    total_sum (int, optional): The running sum of elements that meet the criteria. Defaults to 0.
    count (int, optional): The count of elements that meet the criteria. Defaults to 0.

    Returns:
    tuple: A tuple containing the total sum and count of elements that meet the criteria.
    """
    if len(lst) == 0:
        return total_sum, count
    else:
        element = lst[0]
        if element % 3 == 0 and element >= 10:
            return recursive_sum(lst[1:], total_sum + element, count + 1)
        else:
            return recursive_sum(lst[1:], total_sum, count)