"""
QUESTION:
Implement a stable Counting Sort algorithm in Python to sort a list of integers without using comparisons. The function should be named correct_sort and take a list of integers as input. The function should return the sorted list. The input list may be empty, and the function should handle this case correctly.
"""

def correct_sort(input_list):
    size = len(input_list)
    output = [0] * size

    if size == 0:
        return output

    count = [0] * (max(input_list)+1)
  
    for number in input_list:
        count[number] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(size-1, -1, -1):
        output[count[input_list[i]] - 1] = input_list[i]
        count[input_list[i]] -= 1

    return output