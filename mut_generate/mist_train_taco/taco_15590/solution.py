"""
QUESTION:
Given a string of digits, the task is to check if it is a ‘sum-string’. A string S is called a sum-string if a rightmost substring can be written as a sum of two substrings before it and the same is recursively true for substrings before it. 
 
Example 1:
Input:
12243660
Output:
1
Explanation:
"12243660" is a sum string. As we 
can get, 24 + 36 = 60 & 12 + 24 = 36.
 
Example 2:
Input:
1111112223
Output:
1
Explanation:
"1111112223" is a sum string. As we 
can get, 111+112 = 223 & 1+111 = 112.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isSumString() which takes the string S and returns 1 is S is a sum-string otherwise returns 0.
 
Expected Time Complexity: O(|S|^{2})
Expected Auxiliary Space: O(|S|)
 
Constraints:
1<=|S|<=10^{3}
"""

def is_sum_string(S):
    n = len(S)
    for l in range(1, n):
        sub_arr = int(S[n - l:])
        if is_sum_string_sub(S, n - l, sub_arr, None) == 1:
            return 1
    return 0

def is_sum_string_sub(S, limit, sub_arr, sub_1):
    sub_2 = 0
    if sub_1 is None:
        sub_1 = 0
        for l_1 in range(1, limit + 1):
            sub_1 = int(S[limit - l_1:limit])
            if sub_1 > sub_arr:
                return 0
            for l_2 in range(1, limit - l_1 + 1):
                sub_2 = int(S[limit - l_1 - l_2:limit - l_1])
                if sub_1 + sub_2 > sub_arr:
                    break
                if sub_1 + sub_2 == sub_arr:
                    if limit - l_1 - l_2 == 0:
                        return 1
                    if is_sum_string_sub(S, limit - l_1 - l_2, sub_1, sub_2) == 1:
                        return 1
    else:
        for l_2 in range(1, limit + 1):
            sub_2 = int(S[limit - l_2:limit])
            if sub_1 + sub_2 > sub_arr:
                break
            if sub_1 + sub_2 == sub_arr:
                if limit - l_2 == 0:
                    return 1
                if is_sum_string_sub(S, limit - l_2, sub_1, sub_2) == 1:
                    return 1
    return 0