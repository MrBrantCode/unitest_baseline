"""
QUESTION:
Implement a function named `custom_sort` that sorts the numbers in a given list in descending order while preserving the original positions of duplicates, and sorts the strings in alphabetical order. The function should handle lists containing both numbers and strings, and should not use any built-in sorting functions or libraries.
"""

def custom_sort(lst):
    # Separate numbers and strings
    numbers = [x for x in lst if isinstance(x, (int, float))]
    strings = [x for x in lst if isinstance(x, str)]

    # Sort numbers in descending order
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    # Sort strings in alphabetical order
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i] > strings[j]:
                strings[i], strings[j] = strings[j], strings[i]

    # Merge numbers and strings in the original order
    result = []
    number_index = 0
    string_index = 0
    for elem in lst:
        if isinstance(elem, (int, float)):
            result.append(numbers[number_index])
            number_index += 1
        else:
            result.append(strings[string_index])
            string_index += 1

    return result