"""
QUESTION:
Write a function `second_largest_num_in_range(my_list, my_range)` that finds the second highest value within the given range from the provided list. The list may contain integers and floats, duplicates, and negative numbers, and is not guaranteed to be in any particular order. The function should have a time complexity of O(n log n) and a space complexity of O(n). If there is no second largest number in the given range, the function should return a message indicating this.
"""

def second_largest_num_in_range(my_list, my_range):
    my_list = [num for num in my_list if my_range[0] <= num <= my_range[1]]
    my_list = list(set(my_list))
    my_list.sort(reverse = True)
    if len(my_list) < 2:
        return 'There is no second largest number in the given range'
    else:
        return my_list[1]