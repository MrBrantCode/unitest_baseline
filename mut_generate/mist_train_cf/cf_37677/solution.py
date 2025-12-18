"""
QUESTION:
Write a function `count_A_before_D(S)` that takes a string `S` as input, where `S` consists of characters 'A', 'D', and other characters. The function should return the total number of occurrences of 'A' before each 'D' in the string. The count of 'A' occurrences should reset if a character other than 'A' or 'D' is encountered.
"""

def count_A_before_D(S):
    cnt_a = 0  
    ans = 0  
    for i in range(len(S)):
        if S[i] == 'A':
            cnt_a += 1  
        elif S[i] == 'D':
            ans += cnt_a  
        else:
            cnt_a = 0  
    return ans  