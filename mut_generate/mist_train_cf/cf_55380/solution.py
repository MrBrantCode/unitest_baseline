"""
QUESTION:
Construct a function `multi_arrange` that accepts an ensemble of arrays. The function should return a list of dictionaries, each containing information about an array: its ordinal position ('array'), the maximal index of an element in the array which is not superior to or equal to its antecedent ('index'), and the index of the following less significant element within the same array that can be transchanged with it to hypothetically correct the sequence ('swap_with'). If no such element exists, the corresponding dictionary should contain -1 for all three keys. The input arrays are guaranteed to be non-empty and contain no duplicate values.
"""

def multi_arrange(arrs):
    result = []

    for i, arr in enumerate(arrs, start=1):
        max_index = -1
        swap_with = -1

        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                max_index = j
                break

        if max_index != -1:
            for k in range(max_index + 1, len(arr)):
                if arr[k] < arr[max_index]:
                    swap_with = k
                    break

        result.append({'array': i, 'index': max_index, 'swap_with': swap_with})

    return result