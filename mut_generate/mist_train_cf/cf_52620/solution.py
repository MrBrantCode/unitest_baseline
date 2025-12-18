"""
QUESTION:
Create a function named `within_thresholds_and_average` that takes a list of integers and two thresholds as input. The function should return `True` if all integers in the list are within the given thresholds (inclusive) and print the average of these integers. Otherwise, it should return `False`.
"""

def within_thresholds_and_average(numbers: list, threshold1: int, threshold2: int) -> bool:
    """Return True if every integer in list numbers is between defined thresholds threshold1 and threshold2 (inclusive), and print the average of these integers."""

    # Checking if all elements of the list are within the given thresholds
    if all(threshold1 <= i <= threshold2 for i in numbers):
        # If true, calculate and print the average of these numbers
        avg = sum(numbers) / len(numbers)
        print("Average:", avg)
        return True
    else:
        return False