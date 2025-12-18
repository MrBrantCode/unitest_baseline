"""
QUESTION:
Write a function `top_five_most_frequent` that takes a list of integers as input and returns the top 5 most frequent integers in the list. The output list should be sorted in descending order based on the frequencies of the integers. If two integers have the same frequency, they should be sorted in descending order. If there are less than 5 integers in the list, return all of them.
"""

def top_five_most_frequent(nums):
    """
    Returns the top 5 most frequent integers in the list.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The top 5 most frequent integers in descending order of frequency.
    """
    # Count the frequency of each integer
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Sort the integers based on frequency and value
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))

    # Return the top 5 most frequent integers
    return [x[0] for x in sorted_freq[:5]]