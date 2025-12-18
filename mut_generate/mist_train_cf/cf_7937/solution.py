"""
QUESTION:
Write a function named longest_common_subsequence that takes two input strings and returns their longest common subsequence (LCS), a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. 

The function should throw a NullInputException if both input strings are null and an InvalidInputException if either or both of the input strings are empty. If there is no common subsequence between the two input strings, the function should return an empty string.
"""

class NullInputException(Exception):
    def __init__(self):
        self.message = "Both input strings are null."
        super().__init__(self.message)


class InvalidInputException(Exception):
    def __init__(self):
        self.message = "Input strings must not be empty."
        super().__init__(self.message)


def longest_common_subsequence(str1, str2):
    if str1 is None and str2 is None:
        raise NullInputException()
    if str1 == "" or str2 == "":
        raise InvalidInputException()

    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    lcs = [""] * lcs_length
    i, j = m, n

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs)