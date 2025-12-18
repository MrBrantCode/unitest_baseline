"""
QUESTION:
Create a function named `longest_common_subsequence` that takes two input strings `str1` and `str2` and returns the longest common subsequence (LCS) of the two strings. The function should throw a custom exception `NullInputException` if both input strings are `None`, and throw another custom exception `InvalidInputException` if either input string is empty. The function should handle cases where there is no common subsequence between the two input strings and return an empty string.
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