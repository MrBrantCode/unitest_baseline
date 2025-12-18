"""
QUESTION:
Write a function named `find_most_frequent_value` that finds the most frequent value in a list containing up to 10 million elements, where each element can be either a string of up to 1000 characters or an integer. The function should return the most frequent value as a string if it is a string, and as an integer if it is an integer.
"""

from collections import Counter

def find_most_frequent_value(mylist):
    # Count the occurrences of each element in the list
    count = Counter(mylist)
    
    # Find the element(s) with the maximum count
    most_common = count.most_common(1)
    
    # Get the value and count of the most frequent element
    most_frequent_value, frequency = most_common[0]
    
    # Check if the most frequent value is a string or integer
    if isinstance(most_frequent_value, str):
        return most_frequent_value
    else:
        return int(most_frequent_value)