"""
QUESTION:
Create a function `cubic_function` that takes a list of integers as input and returns a list of all possible sums of three elements from the input list, with a time complexity of O(n^3), where n is the size of the input list. The function should use three nested loops to achieve this.
"""

def cubic_function(input_list):
    result = []
    n = len(input_list)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result.append(input_list[i] + input_list[j] + input_list[k])
    return result