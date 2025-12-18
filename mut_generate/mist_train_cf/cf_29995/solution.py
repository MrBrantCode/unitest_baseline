"""
QUESTION:
Write a function `find_most_frequent_element(nearest_neighbours)` that takes a list of integers `nearest_neighbours` as input and returns the most frequently occurring element in the list. The function should iterate through the input list to determine the frequency of each element.
"""

def find_most_frequent_element(nearest_neighbours):
    labels = {}  
    for i in range(len(nearest_neighbours)):
        if nearest_neighbours[i] not in labels:
            labels[nearest_neighbours[i]] = 1  
        else:
            labels[nearest_neighbours[i]] += 1  
    most_frequent_element = max(labels, key=labels.get)  
    return most_frequent_element