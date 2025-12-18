"""
QUESTION:
Write a function `reverse_last_three` that takes a list of strings as input and modifies it by replacing the last three items with the reverse of those strings, such that the last item becomes first among the three and its individual characters are also reversed. If the list has fewer than three items, do not modify it.
"""

def reverse_last_three(lst):
    """
    This function takes a list of strings as input, modifies it by replacing the last three items 
    with the reverse of those strings, such that the last item becomes first among the three and 
    its individual characters are also reversed. If the list has fewer than three items, do not modify it.

    Args:
        lst (list): A list of strings.

    Returns:
        list: The modified list.
    """
    if len(lst) >= 3:
        # Extract the last three items and reverse the order
        last_three_words = lst[-3:][::-1]
        
        # Reverse the order of characters in each of the last three words
        last_three_words_reversed = [word[::-1] for word in last_three_words]
        
        # Replace the last three items in the original list with the reversed words
        lst[-3:] = last_three_words_reversed
    return lst