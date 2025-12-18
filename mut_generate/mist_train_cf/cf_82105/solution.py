"""
QUESTION:
Create a function named `sort_combined_count` that takes three lists of integers `x`, `y`, and `z` as input and returns a dictionary. The dictionary should contain elements from list `x` as keys and their combined occurrence counts from lists `x`, `y`, and `z` as values. The function should return the dictionary sorted by the highest count in descending order.
"""

def sort_combined_count(x, y, z):
    # Combine all lists into one list
    combined = x + y + z

    # Create a dictionary with the frequency of each number in the combined list
    frequency_dict = {}
    for num in combined:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    # Sort the dictionary by value in descending order and return it
    return dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))