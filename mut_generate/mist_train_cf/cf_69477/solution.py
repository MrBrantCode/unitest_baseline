"""
QUESTION:
Write a function named `frequency_sort` that takes a sorted list of items as input. The function should return a list of tuples, where each tuple contains an item from the input list and its frequency. The output list should be sorted by the frequency of each item in descending order, and for items with the same frequency, they should be sorted by their values in ascending order.
"""

def frequency_sort(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    freq_lst = [(key, value) for key, value in count_dict.items()]
    freq_lst = sorted(freq_lst, key= lambda x: (-x[1], x[0]))
    return freq_lst