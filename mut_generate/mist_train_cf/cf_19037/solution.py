"""
QUESTION:
Create a function named `manipulate_list` that takes a list of integers as input. For each integer in the list, apply the following transformations: if it's divisible by 3, multiply by 2 and add 1; if it's divisible by 5, divide by 2 and subtract 1; if it's divisible by 7, add 5; otherwise, add 3. Return a new list with the transformed integers. The function must have a time complexity of O(n), where n is the length of the input list.
"""

def manipulate_list(input_list):
    output_list = []
    for integer in input_list:
        if integer % 3 == 0:
            output_list.append(integer * 2 + 1)
        elif integer % 5 == 0:
            output_list.append(integer // 2 - 1)
        elif integer % 7 == 0:
            output_list.append(integer + 5)
        else:
            output_list.append(integer + 3)
    return output_list