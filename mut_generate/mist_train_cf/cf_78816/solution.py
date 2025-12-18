"""
QUESTION:
Write a function `identify_elements` that takes a list of elements as input and returns two lists: the three most frequently occurring elements and the three least frequently occurring elements in the list.
"""

from collections import Counter

def identify_elements(data):
    # Count the frequency of each element
    count_data = Counter(data)
    
    # Get the three most common elements
    most_common = count_data.most_common(3)
    
    # Get the three least common elements
    least_common = count_data.most_common()[:-4:-1]
    
    return most_common, least_common