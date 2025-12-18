"""
QUESTION:
Implement a function named `sort` that manually sorts a list of integers in ascending order without using built-in sorting functions. The function should check for non-integer values in the list and print a message "Non-integer found: <value>" if any are found, then terminate the function without sorting the list. If the list contains only integers, the function should sort the list in-place and the sorted list can be printed afterwards.
"""

def sort(input_list):
    for i in range(len(input_list)):
        if not isinstance(input_list[i], int):
            print(f"Non-integer found: {input_list[i]}")
            return
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i-1
        while j >=0 and key < input_list[j] :
            input_list[j+1] = input_list[j]
            j -= 1
        input_list[j+1] = key