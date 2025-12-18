"""
QUESTION:
Create a function `get_positive_and_sort` that takes a list of integers as input and returns a new list containing only the positive numbers from the original list, sorted in ascending order. The function should use a helper function `swap_elements` to swap the positions of two elements in the list. Implement the `swap_elements` function and rectify any errors in the provided code to achieve the desired output.
"""

def get_positive_and_sort(l: list):
    """Return only positive numbers in the list, sorted in ascending order."""

    def swap_elements(n: list, index1: int, index2: int):
        n[index1], n[index2] = n[index2], n[index1]

    positive_list = []
    for num in l:
        if num > 0:
            positive_list.append(num)

    for i in range(len(positive_list)):
        min_index = i
        for j in range(i+1, len(positive_list)):
            if positive_list[min_index] > positive_list[j]:
                min_index = j
        swap_elements(positive_list, i, min_index)
        
    return positive_list