"""
QUESTION:
Implement a function named `common` that takes two lists `l1` and `l2` as input and returns a list of unique common elements in sorted order. The function should not use built-in Python list functions for sorting and removing duplicates.
"""

def common(l1: list, l2: list):
    def sort_list(l: list) -> list:
        n = len(l)

        for i in range(n-1):
            for j in range(n-i-1):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
        return l

    def remove_duplicates(l: list) -> list:
        unique_list = []
        for num in l:
            if num not in unique_list:
                unique_list.append(num)
        return unique_list

    result = [num for num in l1 if num in l2]
    return remove_duplicates(sort_list(result))