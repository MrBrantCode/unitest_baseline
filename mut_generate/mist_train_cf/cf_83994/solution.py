"""
QUESTION:
Write a function named `longest_substring` that takes a list of strings as input and returns the longest common substring among all the strings in the list. If the input list is empty, return `None`. The function should be able to handle a list of strings where some strings may be shorter than the others.
"""

from typing import List, Optional

def longest_substring(strings: List[str]) -> Optional[str]:
    n = len(strings)

    if n == 0:
        return None
    
    shortest_str = min(strings, key=len)
    m = len(shortest_str)
    strs_filtered = [s for s in strings if len(s) >= m]

    lcs_c = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                lcs_c[i][j] = 0
            elif strs_filtered[i-1] == shortest_str[j-1]:
                lcs_c[i][j] = lcs_c[i-1][j-1] + 1
            else:
                lcs_c[i][j] = max(lcs_c[i-1][j], lcs_c[i][j-1])

    index = lcs_c[n][m]

    lcs = [""] * (index+1)
    lcs[index] = "" 

    i, j = n, m
    while i > 0 and j > 0:
        if shortest_str[j-1] == strs_filtered[i-1]:
            lcs[index-1] = strs_filtered[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs_c[i-1][j] > lcs_c[i][j-1]:
            i -= 1
        else:
            j -= 1

    lcs_found = "".join(lcs)

    if lcs_found == "":
        return None
    else:
        return lcs_found