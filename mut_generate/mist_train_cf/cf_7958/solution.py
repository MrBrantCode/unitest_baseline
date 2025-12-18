"""
QUESTION:
Implement a function called "sort_list" that takes two lists as arguments: a list of numbers and a list of strings. The function should return a sorted list that combines the input lists. The numbers should be sorted in descending order. The strings should be sorted based on the sum of the ASCII values of their characters in ascending order. The function should handle duplicate numbers and strings properly during sorting.
"""

def sort_list(num_list, string_list):
    num_list.sort(reverse=True)

    sums = []
    for string in string_list:
        total = 0
        for char in string:
            total += ord(char)
        sums.append(total)

    string_list = [x for _, x in sorted(zip(sums, string_list))]
    sorted_list = num_list + string_list
    return sorted_list