"""
QUESTION:
Create a function called `reversedAddition` that takes two integers as input, where each integer is the reverse of a number. The function should reverse each integer to obtain the original numbers, add them together, and return the sum. The input integers are assumed to be non-negative and the output should be the exact sum of the reversed numbers without reversing the result.
"""

def reversedAddition(reverseOrder1, reverseOrder2):
    """
    This function takes two integers as input, where each integer is the reverse of a number.
    It reverses each integer to obtain the original numbers, adds them together, and returns the sum.

    Args:
        reverseOrder1 (int): The first reversed integer.
        reverseOrder2 (int): The second reversed integer.

    Returns:
        int: The sum of the reversed numbers.
    """
    # Convert the integers to strings, reverse the strings, and convert back to integers
    firstNum = int(str(reverseOrder1)[::-1])
    secondNum = int(str(reverseOrder2)[::-1])

    # Add the reversed numbers and return the result
    return firstNum + secondNum