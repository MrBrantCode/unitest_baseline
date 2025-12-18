"""
QUESTION:
Write a function called `cubic_function` that takes an input list and returns a list containing the sum of every triple combination of elements in the input list. The function should have a time complexity of O(n^3), where n is the size of the input list.
"""

def cubic_function(input_list):
    result = []
    n = len(input_list)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result.append(input_list[i] + input_list[j] + input_list[k])
    return result