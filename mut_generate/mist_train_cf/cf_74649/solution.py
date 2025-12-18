"""
QUESTION:
Write a function `second_highest_frequency(lst, range)` that finds the second highest value within a given range in list `lst` and returns this value along with its frequency in `lst`. The range is inclusive, meaning it includes both the start and end values.
"""

def second_highest_frequency(lst, range):
    # filter the list using the range
    filtered_lst = [x for x in lst if x >= range[0] and x <= range[1]]
    # get a set of unique values
    unique_values = set(filtered_lst)
    # if there's only one unique value, return that value and its frequency
    if len(unique_values) == 1:
        return list(unique_values)[0], filtered_lst.count(list(unique_values)[0])
    # sort the unique values in descending order
    sorted_values = sorted(unique_values, reverse=True)
    # the second highest value is now at position 1
    second_highest = sorted_values[1]
    # count the frequency of the second highest value
    frequency = filtered_lst.count(second_highest)
    return second_highest, frequency