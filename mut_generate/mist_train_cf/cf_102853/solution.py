"""
QUESTION:
Write a function named `most_frequent_value` that takes a list containing integers and/or strings as input and returns the most frequent value. The return value should be a string if the most frequent value is a string, and an integer if the most frequent value is an integer.
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