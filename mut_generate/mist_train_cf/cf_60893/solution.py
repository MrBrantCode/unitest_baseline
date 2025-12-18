"""
QUESTION:
Write a function `countPalindromes(s)` that takes a string `s` of length `N` as input and returns a dictionary where the keys are unique palindromic substrings of `s` and the values are their corresponding frequencies. The function should have a time complexity of O(N^2) and a memory complexity of O(N^2).
"""

def countPalindromes(s):
    dp = [[False]*len(s) for _ in range(len(s))]
    count_dict = {}

    for i in range(len(s)):
        dp[i][i] = True
        if s[i] in count_dict:
            count_dict[s[i]] += 1
        else:
            count_dict[s[i]] = 1

    for curr_len in range(2,len(s)+1): 
        for i in range(len(s) - curr_len + 1):
            end = i + curr_len
            if s[i] == s[end-1]:
                if curr_len == 2:
                    dp[i][end - 1] = True
                else:
                    dp[i][end - 1] = dp[i + 1][end - 2]
            if dp[i][end - 1] == True:
                temp_string = s[i:end]
                if temp_string in count_dict:
                    count_dict[temp_string] += 1
                else:
                    count_dict[temp_string] = 1
    return count_dict