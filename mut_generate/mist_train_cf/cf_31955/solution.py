"""
QUESTION:
Implement a function named `process_input` that takes a list of strings as input where each string contains space-separated values. The function should process the input lines as follows:

- If a line contains only integers separated by spaces, store the integers as a list.
- If a line is empty, append the current list of integers to a result list and clear the current list.
- If a line contains non-integer characters, ignore the line.

Return the result list containing lists of integers. The function should handle the case where the input list ends with a non-empty current list of integers.
"""

def process_input(input_lines):
    result = []
    current_list = []

    for line in input_lines:
        if line.strip() == "":
            if current_list:
                result.append(current_list)
                current_list = []
        else:
            try:
                integers = [int(i) for i in line.strip().split()]
                current_list.extend(integers)
            except ValueError:
                pass

    if current_list:
        result.append(current_list)

    return result