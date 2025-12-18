"""
QUESTION:
Write a function `find_even_numbers` that takes a list of integers as input and returns a tuple. The first element of the tuple is a list of tuples, where each tuple contains the index and value of every even integer in the input list. The second element of the tuple is the total count of even numbers in the list. If there are no even numbers, return the message "No even numbers in the list". The function should be efficient and able to handle large lists and negative numbers.
"""

def find_even_numbers(nums):
    """
    This function takes a list of integers as input and returns a tuple. 
    The first element of the tuple is a list of tuples, where each tuple contains 
    the index and value of every even integer in the input list. The second element 
    of the tuple is the total count of even numbers in the list. If there are no 
    even numbers, return the message "No even numbers in the list".

    Args:
        nums (list): A list of integers.

    Returns:
        tuple: A tuple containing a list of tuples with indices and values of even numbers, 
        and the total count of even numbers. If no even numbers are found, returns a string message.
    """

    even_numbers = [(idx, num) for idx, num in enumerate(nums) if num % 2 == 0]
    count_of_even_numbers = len(even_numbers)

    if count_of_even_numbers == 0:
        return "No even numbers in the list"
    else:
        return (even_numbers, count_of_even_numbers)