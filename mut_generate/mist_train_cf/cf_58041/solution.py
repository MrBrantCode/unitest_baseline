"""
QUESTION:
Write a function named `fixed_function` that takes a list of integers as input. The function should return a string of comma-separated values. If the input list is empty, the function should return "Error: The list is empty." If the list contains non-integer values, the function should return an error message indicating that the list should only contain integers and include the detail of the error.
"""

def fixed_function(in_list):
    if not in_list:               # checking if the list is empty
        return "Error: The list is empty."
    else: 
        try:
            return ", ".join(str(i) for i in list(in_list))   # converting integer to string before joining
        except Exception as e:
            return f"Error: The list should only contain integers. Detail: {str(e)}"