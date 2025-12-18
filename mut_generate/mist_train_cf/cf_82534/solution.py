"""
QUESTION:
Write a function called `calculate_statistics` that takes a list of integers as input. The function should calculate and return the sum, product, and average of the input list, as well as the three smallest and three largest numbers in the list. The input list will contain at least 3 numbers.
"""

def calculate_statistics(numbers):
    """
    Calculate and return the sum, product, average, three smallest, and three largest numbers in the input list.

    Args:
        numbers (list): A list of integers.

    Returns:
        dict: A dictionary containing the sum, product, average, three smallest, and three largest numbers.
    """
    # Calculate sum
    total = sum(numbers)

    # Calculate product
    product = 1
    for n in numbers:
        product *= n

    # Calculate average
    average = total / len(numbers)

    # Find the three largest and three smallest numbers
    numbers.sort()
    three_smallest = numbers[:3]
    three_largest = numbers[-3:]

    # Return the results
    return {
        "sum": total,
        "product": product,
        "average": average,
        "three_smallest": three_smallest,
        "three_largest": three_largest,
    }