"""
QUESTION:
Create a function named `process_strings` that takes a list of strings as input and returns the list of unique strings with no duplicates. Additionally, the function should also display the top 3 most occurring strings in the original list in descending order of their counts. If there are multiple strings with the same count, they should be displayed in lexicographical order.
"""

from collections import Counter

def process_strings(strings):
    """
    This function takes a list of strings, removes duplicates, 
    and displays the top 3 most occurring strings in descending order.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A list of unique strings with no duplicates.
    """
    # Remove duplicates
    unique_strings = list(set(strings))
    
    # Count occurrences of each string
    strings_counts = Counter(strings)
    
    # Display top 3 most occurring strings
    sorted_counts = sorted(strings_counts.items(), key=lambda x: (-x[1], x[0]))
    top3 = sorted_counts[:3]
    for string, count in top3:
        print(f"{string}: {count} occurrences")
        
    return unique_strings