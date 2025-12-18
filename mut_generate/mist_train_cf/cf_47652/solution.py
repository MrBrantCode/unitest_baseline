"""
QUESTION:
Create a function `make_palindrome(s)` that takes a string `s` as input. The function should return a tuple containing the minimum number of insertions required to make the input string a palindrome (ignoring non-alphanumeric characters and considering case sensitivity) and the resulting palindrome string. The palindrome string should be created by inserting the minimum number of characters necessary to make it a palindrome. If the original string is already a palindrome, return 0 and the original string.
"""

def make_palindrome(s):
    s_filtered = ''.join(e for e in s if e.isalnum())
    if s_filtered == s_filtered[::-1]:
        return 0, s

    dp = [[0 for _ in range(len(s_filtered) + 1)] for __ in range(len(s_filtered) + 1)]
    len_s_filtered = len(s_filtered)

    for l in range(2, len_s_filtered + 1):
        i = 0
        j = l - 1
        while j < len_s_filtered:
            if s_filtered[i] == s_filtered[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
            i += 1
            j += 1

    i = 0
    j = len_s_filtered - 1
    palindrome = ""
    while i <= j:
        if s_filtered[i] == s_filtered[j]:
            palindrome += s_filtered[i]
            i += 1
            j -= 1
        elif dp[i][j] == dp[i + 1][j] + 1:
            palindrome += s_filtered[i]
            i += 1
        else:
            palindrome += s_filtered[j]
            j -= 1

    palindrome += palindrome[::-1]

    if len_s_filtered % 2 == 0:
        answer = palindrome[0:len_s_filtered//2] + s_filtered[len_s_filtered//2] + palindrome[len_s_filtered//2:]
    else:
        answer = palindrome

    return dp[0][len_s_filtered - 1], answer