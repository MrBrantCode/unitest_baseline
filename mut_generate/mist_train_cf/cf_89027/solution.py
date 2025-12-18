"""
QUESTION:
Write a function called `mergeSort(records)` that sorts a list of employee records by salary in descending order. If two employees have the same salary, they should be sorted by age in ascending order. The function should have a time complexity of O(n log n), where n is the number of employees in the list. Each employee record is a dictionary with the keys 'name', 'age', 'salary', and 'department'.
"""

def mergeSort(records):
    if len(records) <= 1:
        return records

    middle = len(records) // 2
    left_half = records[:middle]
    right_half = records[middle:]

    sorted_left = mergeSort(left_half)
    sorted_right = mergeSort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]['salary'] > right[j]['salary']:
            result.append(left[i])
            i += 1
        elif left[i]['salary'] < right[j]['salary']:
            result.append(right[j])
            j += 1
        else:
            if left[i]['age'] <= right[j]['age']:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result