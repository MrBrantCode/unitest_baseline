"""
QUESTION:
Write a function `count_occurrences(array)` that finds the number of occurrences of each time value in the given array and determines the positions of each occurrence. The function should return a tuple of two dictionaries. The first dictionary should have time values as keys and their corresponding counts as values, and the second dictionary should have time values as keys and lists of their positions as values. The function should have a time complexity of O(n) and space complexity of O(n), where n is the length of the array.
"""

def count_occurrences(array):
    time_count = {}  
    time_positions = {}  
    
    for i in range(len(array)):
        time = array[i]
        if time in time_count:
            time_count[time] += 1
            time_positions[time].append(i)
        else:
            time_count[time] = 1
            time_positions[time] = [i]
    
    return time_count, time_positions