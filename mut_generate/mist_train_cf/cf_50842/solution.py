"""
QUESTION:
Create a function called `eliminate_repeats` that takes a list of integers as input and returns a tuple. The tuple should contain a list with all repeating elements removed, keeping only the last occurrence of each integer, and a dictionary with the count of each integer in the original list. The returned list should maintain the original order of elements.
"""

def eliminate_repeats(array):
    repeat_count = {}
    purged_list = []
    reversed_array = array[::-1] # reverse the array
    
    # check the list from right to left and add to purged list if it's not already there
    for number in reversed_array:
        if number not in purged_list:
            purged_list.append(number)
        # update the repeat count dictionary
        if number in repeat_count:
            repeat_count[number] += 1
        else:
            repeat_count[number] = 1
    
    purged_list.reverse() # reverse the purged list back to its original order
    return purged_list, repeat_count