"""
QUESTION:
Create a function named `rotate_list` that takes a list of numerical variables and an optional 'direction' argument as input. The function should rotate the list in the specified direction. If the direction is 'left', the function should remove the minimum value from the list and append it to the end. If the direction is 'right', the function should remove the maximum value from the list and insert it at the start. If the direction is neither 'left' nor 'right', the function should handle this as an error. The function should also handle any other potential exceptions that may occur. The 'direction' argument defaults to 'left' if not specified.
"""

def rotate_list(num_list, direction='left'):
    try:
        if direction == 'left':
            min_val = min(num_list)
            num_list.remove(min_val)
            num_list.append(min_val)
        elif direction == 'right':
            max_val = max(num_list)
            num_list.remove(max_val)
            num_list.insert(0, max_val)
        else:
            print(f'Invalid direction "{direction}" specified. Must be either "left" or "right".')
    except Exception as e:
        print(f'An error occurred: {e}')
    return num_list