"""
QUESTION:
Write a function to input a specified number of integers from the user. The function should take the number of integers as input and return a list of integers. Restrict the input to non-negative integers and ensure that the user inputs the exact number of integers requested.
"""

def entrance(n):
    """Input a specified number of integers from the user.

    Args:
    n (int): The number of integers to input.

    Returns:
    list: A list of n non-negative integers.

    Raises:
    ValueError: If the user inputs non-integer values or less/more integers than requested.
    """

    while True:
        user_input = input(f"Enter {n} numbers: ")
        try:
            numbers = list(map(int, user_input.split()))
            if len(numbers) == n and all(num >= 0 for num in numbers):
                return numbers
            else:
                print("Invalid input. Please enter the exact number of non-negative integers.")
        except ValueError:
            print("Invalid input. Please enter integers only.")