"""
QUESTION:
Write a function `solve(input_list)` that sorts a given 2D array of integers in ascending order. The function should sort each sub-array independently and then sort the entire 2D array based on the average of the elements in each sub-array. The function should not use any built-in sort functions. The input list can contain both integers and lists of integers.
"""

def solve(input_list):
    subarrays = [element for element in input_list if isinstance(element, list)]
    normal_elements = [element for element in input_list if not isinstance(element, list)]

    def bubble_sort(l):
        n = len(l)
        for i in range(n):
            for j in range(0, n - i - 1):
                if l[j] > l[j + 1] :
                    l[j], l[j + 1] = l[j + 1], l[j]
        return l

    def average(l):
        return sum(l) / len(l)

    sorted_subarrays = sorted([bubble_sort(subarray) for subarray in subarrays], key=average)
    sorted_elements = bubble_sort(normal_elements)
    return sorted_subarrays + sorted_elements