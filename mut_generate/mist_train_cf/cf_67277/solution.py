"""
QUESTION:
Create a function called `shift_elements` that takes a list of integers as input and returns a list of lists, where each inner list represents the state of the input list after a left shift operation. The function should perform a left shift operation N times, where N is the number of elements in the input list, and maintain the order of adjacent elements. The function should return all intermediate states of the list after each shift.
"""

def shift_elements(input_list):
    result = []
    list_length = len(input_list)
    for i in range(list_length):
        input_list = input_list[1:] + [input_list[0]]
        result.append(input_list)
    return result