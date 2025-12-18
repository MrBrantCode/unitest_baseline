"""
QUESTION:
Implement a function `sort_data` that sorts a given list of integers in ascending order. The function should take a list of integers as input, sort it in-place, and return the sorted list.
"""

def sort_data(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
       
    return data