"""
QUESTION:
Create a function called `frequency_priority` that accepts two parameters: `main_list` and `priority_list`, both of which are lists of numeric values. The function should return a dictionary where the keys are the unique elements from `main_list` and the values are their corresponding frequencies. The frequency of elements that appear in both `main_list` and `priority_list` should be doubled. The dictionary should be sorted in descending order by frequency, and for elements with the same frequency, they should be sorted in ascending order by their numeric value. The function should also handle cases where `main_list` or `priority_list` are not valid lists of numeric values.
"""

def frequency_priority(main_list, priority_list):
    if not (isinstance(main_list, list) and all(isinstance(item, (int, float)) for item in main_list)):
        return "Invalid main list"

    if not (isinstance(priority_list, list) and all(isinstance(item, (int, float)) for item in priority_list)):
        return "Invalid priority list"

    frequency = {}
    for num in main_list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    for num in priority_list:
        if num in frequency:
            frequency[num] *= 2

    sorted_frequency = {k: v for k, v in sorted(frequency.items(), key=lambda item: (-item[1], item[0]))}

    return sorted_frequency