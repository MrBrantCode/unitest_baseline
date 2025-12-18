"""
QUESTION:
Implement a function called `count_occurrences` that takes an array of time strings as input and returns a dictionary where each key is a unique time string and its corresponding value is a list containing the count of occurrences and a list of positions where the time string appears in the array. The function should have a time complexity of O(n) and space complexity of O(n), where n is the length of the array.
"""

def count_occurrences(array):
    time_dict = {}  

    for i, time in enumerate(array):
        if time in time_dict:
            time_dict[time][0] += 1
            time_dict[time][1].append(i)
        else:
            time_dict[time] = [1, [i]]  

    return time_dict