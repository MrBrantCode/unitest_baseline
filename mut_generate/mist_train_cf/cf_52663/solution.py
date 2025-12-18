"""
QUESTION:
Create a function named `rotate_list` that takes two parameters: a list (`my_list`) and the number of positions to rotate the list to the right. The function should return the rotated list. The rotation should be handled circularly, meaning if the number of positions is greater than the length of the list, it should find the equivalent position within the length of the list.
"""

def rotate_list(my_list, positions):
    # If the number of positions is greater than the length of the list,
    # find the equivalent position within the length of the list
    positions %= len(my_list)
    
    # Slice the list at the specified position and join the two parts in reversed order.
    return my_list[-positions:] + my_list[:-positions]