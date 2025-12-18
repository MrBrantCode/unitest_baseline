"""
QUESTION:
Given an array of numbers and an interval, implement the `second_highest_within_range` function that returns the second highest numerical value within the specified interval in the array. The interval is defined as [inclusive start, inclusive end]. If there are less than 2 distinct numbers within the interval, the function should return `None`.
"""

def second_highest_within_range(arr, interval):
    # apply the interval to the array by checking if each value is within interval
    arr = [x for x in arr if interval[0] <= x <= interval[1]]

    # remove duplicates
    arr = list(set(arr))

    # check if there are at least 2 elements in the array
    if len(arr) < 2: 
        return None

    # sort the array in descending order
    arr.sort(reverse=True)

    # return the second element in the sorted array
    return arr[1]