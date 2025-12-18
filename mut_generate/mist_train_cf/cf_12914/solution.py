"""
QUESTION:
Create a function called `histogram_chart` that takes a list of integers as input and returns a string representing a histogram chart where the numbers 0-9 are on the x-axis and their frequencies are on the y-axis, represented by asterisks (*). The input list contains single-digit integers.
"""

def histogram_chart(nums):
    """
    Creates a histogram chart of single-digit integers.

    Args:
    nums (list): A list of single-digit integers.

    Returns:
    str: A string representing a histogram chart.
    """

    # Initialize a dictionary to store the frequency of each number
    freq = {i: 0 for i in range(10)}

    # Count the frequency of each number
    for num in nums:
        freq[num] += 1

    # Create the histogram chart
    chart = ""
    for i in range(10):
        chart += f"{i}\t{'*' * freq[i]}\n"

    return chart