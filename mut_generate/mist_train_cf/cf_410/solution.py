"""
QUESTION:
Implement a function `sum_of_multiples_of_three` that calculates the sum of all elements in a list that are multiples of 3. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the size of the input list. The function should not use any built-in functions or libraries to calculate the sum or check if a number is a multiple of 3. The input list can contain positive and negative integers, duplicates, and the function should handle large input sizes efficiently.
"""

def sum_of_multiples_of_three(numbers):
    """
    Calculate the sum of all elements in a list that are multiples of 3.

    Args:
    numbers (list): A list of integers.

    Returns:
    int: The sum of all elements in the list that are multiples of 3.

    Time complexity: O(n), where n is the size of the input list.
    Space complexity: O(1), excluding the input list.
    """
    sum_of_multiples = 0
    for num in numbers:
        if num % 3 == 0:
            sum_of_multiples += num
    return sum_of_multiples