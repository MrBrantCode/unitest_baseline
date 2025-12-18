"""
QUESTION:
Write a function `most_frequent_name` that finds the most frequent name in a given array of names, considering the names as case-insensitive. The function should be able to handle an array of up to 10^6 names, where each name can be up to 100 characters long and may contain special characters. The function should have a time complexity of O(n), where n is the number of names in the array.
"""

def most_frequent_name(names):
    name_count = {}
    for name in names:
        name = name.lower()
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1
    
    most_frequent = ""
    max_count = 0
    for name, count in name_count.items():
        if count > max_count:
            most_frequent = name
            max_count = count
    
    return most_frequent