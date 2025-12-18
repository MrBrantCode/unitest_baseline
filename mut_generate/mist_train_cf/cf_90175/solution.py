"""
QUESTION:
Implement a function called "sort_list" that takes two lists as arguments: "num_list" containing numbers and "string_list" containing strings. The function should return a single sorted list where the numbers are in descending order and the strings are sorted in ascending order based on the sum of their ASCII values. The function should handle duplicate numbers and strings properly during sorting.
"""

def sort_list(num_list, string_list):
    # Sort the num_list in descending order
    num_list.sort(reverse=True)

    # Calculate the sums of ASCII values for each string
    sums = []
    for string in string_list:
        total = 0
        for char in string:
            total += ord(char)
        sums.append(total)

    # Sort the string_list based on the sums of ASCII values in ascending order
    string_list = [x for _, x in sorted(zip(sums, string_list))]

    # Combine the sorted num_list and string_list into a single list
    sorted_list = num_list + string_list

    # Return the sorted list
    return sorted_list