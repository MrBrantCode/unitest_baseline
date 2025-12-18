"""
QUESTION:
Create a function called `most_frequent_value` that takes a list as input. The list can contain both integers and strings. Return the most frequent value in the list. If the most frequent value is a string, return it as a string. If the most frequent value is not a string, return it as an integer.
"""

def most_frequent_value(mylist):
    count_dict = {}
    for item in mylist:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    max_count = 0
    most_frequent = None
    for item, count in count_dict.items():
        if count > max_count:
            max_count = count
            most_frequent = item
    
    if isinstance(most_frequent, str):
        return most_frequent
    else:
        return int(most_frequent)