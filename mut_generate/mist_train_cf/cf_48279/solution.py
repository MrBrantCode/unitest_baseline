"""
QUESTION:
Implement a function `shell_sort(input_list, key)` that sorts a list of dictionaries in ascending order based on a specific key using the Shell sort algorithm. If the specified key is not present in a dictionary, consider it as having a lower value than the dictionaries with the key. The function should return the sorted list of dictionaries.
"""

def shell_sort(input_list, key):
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            while j >= gap and (key in input_list[j - gap] and key in temp and input_list[j - gap][key] > temp[key]):
                input_list[j] = input_list[j - gap]
                j -= gap
            input_list[j] = temp
        gap //= 2
    return input_list