"""
QUESTION:
Implement a function named `custom_sort(arr1, arr2)` that combines and sorts two given arrays with different data types into one sorted array. The sorting criteria are: 
- Numbers have higher priority than strings.
- Data should be sorted in ascending order for same data types.
- Arrays can contain numeric strings that should be treated as numbers.
The function should not use built-in sorting functions.
"""

def custom_sort(arr1, arr2):
    merged_array = arr1 + arr2

    for i in range(len(merged_array)):
        if isinstance(merged_array[i], str) and merged_array[i].isdigit():
            merged_array[i] = int(merged_array[i])

    numbers = []
    strings = []

    for value in merged_array:
        if isinstance(value, int) or isinstance(value, float):
            numbers.append(value)
        else:
            strings.append(value)

    # bubble sort for the numbers list
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    # bubble sort for the strings list 
    for i in range(len(strings)-1):
        for j in range(len(strings)-i-1):
            if strings[j] > strings[j+1]:
                strings[j], strings[j+1] = strings[j+1], strings[j]

    sorted_array = numbers + strings

    return sorted_array