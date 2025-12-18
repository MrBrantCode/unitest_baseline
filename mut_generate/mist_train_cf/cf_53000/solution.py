"""
QUESTION:
Write a function called `remove_apple` that removes all occurrences of the string "Apple" from a given list of strings without using any built-in functions or methods. The function should return a new list with all "Apple" elements removed.
"""

def remove_apple(input_list):
    output_list = []
    
    # Loop through each element in the input list
    for i in range(len(input_list)):
        # Check if the element is not "Apple"
        if input_list[i] != "Apple":
            # If it's not, add it to the output list
            output_list.append(input_list[i])
    
    return output_list