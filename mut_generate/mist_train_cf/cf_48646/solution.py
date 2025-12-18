"""
QUESTION:
Write a recursive function called `print_thank_you(n, current_num=0)` to output "Thank you" for the first 'n' even numbers, where 'n' is a user-provided input. The function should handle input validation to ensure only positive integer values are accepted for 'n'.
"""

def print_thank_you(n, current_num=0):
    """
    Prints "Thank you" for the first 'n' even numbers.

    Args:
        n (int): The number of even numbers for which to print "Thank you".
        current_num (int): The current number being checked. Defaults to 0.

    Returns:
        None
    """
    # Handle input validation
    if not isinstance(n, int) or n <= 0:
        print("Please enter a positive integer.")
        return
    
    # Base case: stop recursion when n reaches 0
    if n == 0:
        return
    
    # Check if the current number is even
    if current_num % 2 == 0:
        print("Thank you")
        print_thank_you(n-1, current_num + 1)
    else:
        print_thank_you(n, current_num + 1)