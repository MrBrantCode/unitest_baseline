"""
QUESTION:
Write a `find_largest_sum` function that takes a list of integers as input and returns a tuple containing the maximum attainable sum of a subarray and its start and end indices. The subarray should not contain any adjacent elements that are equal or form an arithmetic progression with the next element.
"""

def find_largest_sum(array: list) -> (int, tuple):
    def sum_subarray(start: int, end: int) -> int:
        return sum(array[start:end+1])

    def no_adjacent_elements(start: int, end: int) -> bool:
        prev = array[start]
        for i in range(start + 1, end + 1):
            if array[i] == prev or (i < end and array[i-1]==(array[i]+array[i+1])/2): 
                return False
            prev = array[i]
        return True

    max_sum = 0
    indices = (0, 0)
    for i in range(len(array)):
        for j in range(i, len(array)):
            if no_adjacent_elements(i, j):
                sum_ = sum_subarray(i, j)
                if sum_ > max_sum:
                    max_sum = sum_
                    indices = (i, j)
    return max_sum, indices