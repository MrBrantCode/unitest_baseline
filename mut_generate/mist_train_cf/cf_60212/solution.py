"""
QUESTION:
Implement a function `longest_common_subsequence(s1, s2)` that takes two input strings `s1` and `s2` and returns a tuple containing the length and the longest common subsequence of the two input strings. The function should be efficient and scalable for strings of large length, ideally around 10^6 characters. The time complexity of the function should be as low as possible.
"""

def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)

    dp_table = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp_table[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1] + 1
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

    result = ''
    i, j = m, n

    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            result = s1[i-1] + result
            i -= 1
            j -= 1
        elif dp_table[i-1][j] > dp_table[i][j-1]:
            i -= 1
        else:
            j -= 1

    return len(result), result