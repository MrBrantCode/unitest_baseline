"""
QUESTION:
Write a function named `find_common_subsequence` that takes three character sequences `s1`, `s2`, and `s3` as input and returns the longest common subsequence shared collectively by them. The longest common subsequence does not have to be sequential but must maintain the order of characters within the original sequences. The function should have a time complexity of O(n^3) where n is the length of the input sequences.
"""

def find_common_subsequence(s1, s2, s3):
    len1, len2, len3 = len(s1), len(s2), len(s3)

    dp_table = [[[0 for _ in range(len3+1)] for _ in range(len2+1)] for _ in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            for k in range(1, len3+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    dp_table[i][j][k] = dp_table[i-1][j-1][k-1] + 1
                else:
                    dp_table[i][j][k] = max(dp_table[i-1][j][k], dp_table[i][j-1][k], dp_table[i][j][k-1])

    common_subsequence = ""
    i, j, k = len1, len2, len3

    while dp_table[i][j][k]:
        if s1[i-1] == s2[j-1] == s3[k-1]:
            common_subsequence = s1[i-1] + common_subsequence
            i -= 1
            j -= 1
            k -= 1
        elif dp_table[i][j][k] == dp_table[i-1][j][k]:
            i -= 1
        elif dp_table[i][j][k] == dp_table[i][j-1][k]:
            j -= 1
        else:
            k -= 1

    return common_subsequence