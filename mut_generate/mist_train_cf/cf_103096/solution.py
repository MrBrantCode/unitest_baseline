"""
QUESTION:
Create a function named `shuffle_odd_elements` that takes a list of elements as input. The function should modify the input list by reversing the order of its odd-indexed elements (1-indexed) while keeping the even-indexed elements in their original positions.
"""

def shuffle_odd_elements(arr):
    odd_elements = [arr[i] for i in range(1, len(arr), 2)]
    odd_elements.reverse()
    result = []
    odd_index = 0
    for i in range(len(arr)):
        if i % 2 == 1:
            result.append(odd_elements[odd_index])
            odd_index += 1
        else:
            result.append(arr[i])
    return result