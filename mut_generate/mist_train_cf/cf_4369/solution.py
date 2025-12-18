"""
QUESTION:
Write a function `count_occurrences(array)` that finds the number of occurrences of each time value in the given array and determines the positions of each occurrence. The function should return a dictionary with the count of each time value and another dictionary with the positions of each time value. The function should have a time complexity of O(n) and space complexity of O(n), where n is the length of the array. Note that the function cannot use built-in functions or libraries for time/date manipulation.
"""

def count_occurrences(array):
    time_count = {}  # Hashmap to store the count of each time value
    time_positions = {}  # Hashmap to store the positions of each time value
    
    for i in range(len(array)):
        time = array[i]
        if time in time_count:
            time_count[time] += 1
            time_positions[time].append(i)
        else:
            time_count[time] = 1
            time_positions[time] = [i]
    
    return time_count, time_positions