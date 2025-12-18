"""
QUESTION:
Create a function `calc_average(input_list)` that takes a list of numbers as input and returns the average of the three highest and the three lowest numbers in the list. The function should handle exceptions for lists with less than six numbers or non-numeric data. Efficiency should be maintained for large lists.
"""

import heapq

def calc_average(input_list):
    try:
        if len(input_list) < 6:
            return "The list should have at least six numbers!"

        for i in input_list:
            if not isinstance(i, (int, float)):
                return "The list should have only numeric data!"

        three_largest = heapq.nlargest(3, input_list)
        three_smallest = heapq.nsmallest(3, input_list)

        avg_highest = sum(three_largest) / len(three_largest)
        avg_lowest = sum(three_smallest) / len(three_smallest)

        return avg_highest, avg_lowest
        
    except Exception as e:
        return str(e)