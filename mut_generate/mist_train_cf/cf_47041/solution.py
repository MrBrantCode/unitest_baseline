"""
QUESTION:
Create a function `filter_values` that takes a list of integers and an integer as input, and returns a new list containing only the integers from the original list that are less than or equal to the given integer. The function should handle cases where the input list contains non-numeric values, and print an error message if such values are encountered.
"""

def filter_values(my_list, num):
    filtered_list = []
    for i in my_list:
        try: 
            if i <= num:
                filtered_list.append(i)
        except TypeError:
            print("Error: non-numeric input in the list detected!")
    return filtered_list