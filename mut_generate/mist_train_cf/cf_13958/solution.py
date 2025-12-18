"""
QUESTION:
Write a function called `find_average_even_numbers` that takes a list of integers as input and returns the average of all the even numbers in the list. The function should iterate through the items of the list and only consider even numbers in the calculation. If the list is empty or contains no even numbers, the function should return 0.
"""

def find_average_even_numbers(lst):
    """
    This function calculates the average of all the even numbers in a given list.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    float: The average of all the even numbers in the list. If the list is empty or contains no even numbers, returns 0.
    """
    
    # Initialize sum_of_even_numbers and count_of_even_numbers to 0
    sum_of_even_numbers = 0
    count_of_even_numbers = 0
    
    # Iterate through each number in the list
    for num in lst:
        # Check if the number is even
        if num % 2 == 0:
            # Add the number to sum_of_even_numbers
            sum_of_even_numbers += num
            # Increment count_of_even_numbers
            count_of_even_numbers += 1
    
    # Check if there are any even numbers in the list
    if count_of_even_numbers == 0:
        # If not, return 0
        return 0
    else:
        # If there are even numbers, calculate and return their average
        return sum_of_even_numbers / count_of_even_numbers