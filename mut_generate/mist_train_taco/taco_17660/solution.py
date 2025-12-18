"""
QUESTION:
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:


Input: 12
Output: 21


 

Example 2:


Input: 21
Output: -1
"""

def next_greater_element(n: int) -> int:
    s = [i for i in str(n)]
    exist = -1
    
    for i in range(len(s) - 1, 0, -1):
        if s[i - 1] < s[i]:
            temp = sorted(s[i - 1:])
            pivot = temp.index(s[i - 1])
            for j in range(pivot + 1, len(temp)):
                if temp[j] > s[i - 1]:
                    pivot = j
                    break
            s[i - 1] = temp[pivot]
            del temp[pivot]
            s[i:] = temp
            exist = 1
            break
    
    ret = int(''.join(s))
    if exist == 1 and ret < 2147483647:
        return ret
    else:
        return -1