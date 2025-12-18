"""
QUESTION:
Implement a function `most_frequent_element(lst)` that returns the most frequent element in a list of at most 10^6 integers between 0 and 10^9. The function should only consider elements that appear at least twice and should not use any built-in sorting or counting functions.
"""

def most_frequent_element(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    most_frequent = None
    highest_count = 1
    for num, count in count_dict.items():
        if count >= 2 and count > highest_count:
            highest_count = count
            most_frequent = num
    
    return most_frequent