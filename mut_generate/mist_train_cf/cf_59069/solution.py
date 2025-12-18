"""
QUESTION:
Design two functions, `how_many_times` and `misplaced_count_subsequences`, that take two parameters: `main_str` (the principal string) and `sub_str` (the substring). 

`how_many_times` should calculate the number of occurrences of `sub_str` in `main_str`, considering overlapping instances. 

`misplaced_count_subsequences` should calculate the number of times `sub_str` appears as a subsequence in `main_str`, disregarding overlapping instances. The function should return the count of dislocated subsequences.

The input strings `main_str` and `sub_str` are non-empty and contain only characters. The function should return an integer representing the count of occurrences or subsequences.
"""

def how_many_times(main_str: str, sub_str: str) -> int:
    """
    Identifies the occurrence count of a determined sub-string within the source string. 
    Includes intersecting instances.
    """
    count = start = 0
    while start < len(main_str):
        pos = main_str.find(sub_str, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count


def misplaced_count_subsequences(main_str: str, sub_str: str) -> int:
    """
    Evaluates the count of a given sub-string present as a mislocated subsequence within the primary string. 
    Disregards overlapped instances.
    """
    m, n = len(sub_str), len(main_str)
    lookup = [[0] * (n + 1) for _ in range(m + 1)]

    for j in range(n + 1):
        lookup[0][j] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sub_str[i - 1] == main_str[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + lookup[i][j - 1]
            else:
                lookup[i][j] = lookup[i][j - 1]

    return lookup[m][n]