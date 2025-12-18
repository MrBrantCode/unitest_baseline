"""
QUESTION:
Create a function `remove_last_n_elements` that takes a list and an integer `n` as parameters. The function should eliminate the last `n` elements of the list and return the modified list using recursion, without using any built-in list methods. If `n` is greater than the length of the list, the function should handle the error gracefully and return an error message.
"""

def remove_last_n_elements(lst, n):
    # Handle errors when n is greater than the length of the list
    if n > len(lst):
        return "Error: n is greater than the length of the list!"
    
    # Base cases
    if n == 0 or not lst:
        return lst

    # Recursive case
    else:
        # Define a new list without the last element
        new_list = lst[:-1]

        # Recursively call the function with n decremented by 1
        return remove_last_n_elements(new_list, n-1)