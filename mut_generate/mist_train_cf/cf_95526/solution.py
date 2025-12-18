"""
QUESTION:
Given an array of time values as strings in the format "HH:MM AM/PM", write a function `count_occurrences(array)` that returns a dictionary where the keys are the unique time values in the array and the values are lists containing the count and positions of each time value in the array. The function should have a time complexity of O(n) and space complexity of O(n), where n is the length of the array.
"""

def count_occurrences(array):
    time_dict = {}  # dictionary to store count and positions

    for i, time in enumerate(array):
        if time in time_dict:
            time_dict[time][0] += 1
            time_dict[time][1].append(i)
        else:
            time_dict[time] = [1, [i]]  # [count, positions]

    return time_dict