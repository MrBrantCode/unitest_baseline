"""
QUESTION:
Find a pair of numbers in a collection that, when divided, yield a pre-established quotient. Implement a function called `find_division_pair` that takes a list of decimal numbers and a target quotient as input, and returns a pair of numbers from the list that divide to the target quotient.
"""

def find_division_pair(numbers, target):
    """
    This function finds a pair of numbers in a list that divide to a target quotient.

    Args:
    numbers (list): A list of decimal numbers.
    target (float): The target quotient.

    Returns:
    tuple: A pair of numbers from the list that divide to the target quotient, or None if no such pair exists.
    """

    # Create a set to store the numbers we've seen so far for efficient lookups
    num_set = set()

    # Iterate over the list of numbers
    for num in numbers:
        # Calculate the divisor
        divisor = num / target
        
        # Check if the divisor is in the set
        if divisor in num_set:
            # If it is, return the pair
            return (divisor, num)
        
        # Add the current number to the set
        num_set.add(num)

    # If no pair is found, return None
    return None