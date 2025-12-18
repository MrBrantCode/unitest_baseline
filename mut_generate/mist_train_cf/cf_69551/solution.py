"""
QUESTION:
Create a function `count_number_occurrences` that takes a list `lst` and a number `num` as input, and returns the occurrence of the given number in the list. The function should run in the most efficient time complexity possible.
"""

def count_number_occurrences(lst, num):
    # Create an empty dictionary
    count_map = {}

    # Iterate through each element in the list
    for i in lst:
        # If the element is in the dictionary increment its count
        if i in count_map:
            count_map[i] += 1
        # else, add the element to the dictionary
        else:
            count_map[i] = 1

    # Return the occurrence of the given number, if it's not in the count_map return 0
    return count_map.get(num, 0)