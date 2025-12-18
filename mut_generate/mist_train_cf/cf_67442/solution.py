"""
QUESTION:
Create a function `sort_by_unique_characters` that takes a list of strings as input and returns the list sorted in ascending order based on the number of unique characters in each string.
"""

def sort_by_unique_characters(my_list):
    # Calculate the unique count of characters in each string in the list
    unique_character_counts = [len(set(word)) for word in my_list]
    # Zip together list of strings and counts
    combined = list(zip(my_list, unique_character_counts))
    # Sort combined list by counts
    sorted_list = sorted(combined, key=lambda x: x[1])
    # Extract strings from sorted list and return
    return [word for word, count in sorted_list]