"""
QUESTION:
Create a function named `most_frequent_digit` that accepts an array of unique numerical strings. The function should return the most frequent digit from all defined strings. If multiple digits possess the same frequency, the function should return the digit that appears first.
"""

from collections import Counter, OrderedDict

def most_frequent_digit(num_strings):
    # Merge the list of strings into one string.
    all_digits = ''.join(num_strings)
    
    # Use Counter to count the number of occurrences of each digit
    # and sort them into an ordered dictionary.
    frequency_dict = OrderedDict(sorted(
        Counter(all_digits).items(),
        key=lambda x: all_digits.index(x[0])
    ))
    
    # Find the maximum count.
    max_count = max(frequency_dict.values())
    
    # Return the first digit with the maximum count.
    for digit, count in frequency_dict.items():
        if count == max_count:
            return digit