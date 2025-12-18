"""
QUESTION:
Write a function named `sort_dictionary` that takes a dictionary as input and returns a new dictionary. The returned dictionary should include only the key-value pairs from the input dictionary where the value is divisible by 3 and the key starts with a lowercase letter and ends with an uppercase letter. The key-value pairs in the returned dictionary should be sorted by value in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def sort_dictionary(dictionary):
    """
    Returns a new dictionary containing only the key-value pairs from the input dictionary 
    where the value is divisible by 3 and the key starts with a lowercase letter and ends with an uppercase letter.
    The key-value pairs in the returned dictionary are sorted by value in ascending order.

    Time complexity: O(n log n)
    Space complexity: O(n)

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with the filtered and sorted key-value pairs.
    """
    return dict(sorted({k: v for k, v in dictionary.items() if v % 3 == 0 and k[0].islower() and k[-1].isupper()}.items(), key=lambda item: item[1]))