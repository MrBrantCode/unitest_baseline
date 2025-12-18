"""
QUESTION:
Write a function `find_second_occurrence` that takes two parameters: `string` and `substring`. The function should return the index of the second occurrence of `substring` in `string` using case-sensitive search. The function should return -1 if `substring` occurs less than twice in `string`. The function should achieve a time complexity of O(n) and a space complexity of O(1), where n is the length of `string`.
"""

def find_second_occurrence(string, substring):
    first_occurrence = string.find(substring)
    if first_occurrence == -1:
        return -1
    second_occurrence = string.find(substring, first_occurrence + 1)
    return second_occurrence