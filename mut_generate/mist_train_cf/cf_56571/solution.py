"""
QUESTION:
Create a function `median(my_list)` that calculates the median of a given list of numbers. The function should first sort the list in ascending order, then find the middle value(s). If the list length is odd, return the middle value. If the list length is even, return the average of the two middle values. The function should optimize the calculation process and maintain a time complexity of O(n log n) due to the list sorting operation.
"""

def entance(my_list):
    my_list.sort()
    half = len(my_list) // 2
    if len(my_list) % 2 == 0:   # even number of elements
        return (my_list[half - 1] + my_list[half]) / 2.0
    else:   # odd number of elements
        return my_list[half]