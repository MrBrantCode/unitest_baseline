"""
QUESTION:
Write a function `find_most_frequent_value` that takes a list as input. The list can contain up to 10 million elements, and each element can be an integer or a string of up to 1000 characters. The function should return the most frequent value in the list, preserving its original data type (i.e., return it as a string if it is a string, and as an integer if it is an integer).
"""

from collections import Counter

def find_most_frequent_value(mylist):
    # Count the occurrences of each element in the list
    count = Counter(mylist)
    
    # Find the element(s) with the maximum count
    most_common = count.most_common(1)
    
    # Get the value and count of the most frequent element
    most_frequent_value, frequency = most_common[0]
    
    # Return the most frequent value
    return most_frequent_value