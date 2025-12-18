"""
QUESTION:
Create a function named `get_avg_and_modify_list` that takes a list of numerical arrays and a singular numerical value as arguments. The function should append the given numerical value as the last element to each nested array in the list, and then calculate the average of all the last elements of the modified nested arrays. The function should return the modified list of arrays and the calculated average.
"""

def get_avg_and_modify_list(num_arrays, num):
    # Append the given number num to each nested list
    new_arrays = [arr + [num] for arr in num_arrays]
    
    # Calculate the average of the final elements of the nested lists
    avg = num # Since the final element of each list is the same, its average is the number itself

    return new_arrays, avg