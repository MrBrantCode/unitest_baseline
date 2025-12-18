"""
QUESTION:
Create a function `top_five_frequent` that takes a list of integers as input and returns a list of the top 5 most frequent integers, along with their frequencies, sorted in descending order of frequency and ascending order of value in case of a tie.
"""

def top_five_frequent(nums):
    """
    Returns a list of the top 5 most frequent integers in the input list, 
    along with their frequencies, sorted in descending order of frequency 
    and ascending order of value in case of a tie.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of tuples, where each tuple contains an integer and its frequency.
    """
    from collections import Counter
    count = Counter(nums)
    sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    return sorted_count[:5]