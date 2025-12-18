"""
QUESTION:
Confusing Number Function

Create a function `confusingNumber` that determines if a given number `N` is a "confusing number". A number is considered confusing if it can be rotated 180 degrees to create a new, valid number with each digit remaining valid. The rotation rules are as follows: 0, 1, 6, 8, 9 are transformed into 0, 1, 9, 8, 6 respectively, while 2, 3, 4, 5, and 7 become invalid.

Restrictions: 
- `0 <= N <= 10^9`
- After rotation, leading zeros can be disregarded.
"""

def confusingNumber(N):
    map_lst = {0:0, 1:1, 6:9, 8:8, 9:6}
    res, mul, N_copy = 0, 1, N
        
    while(N > 0):
        if N % 10 in map_lst:
            res = res + (map_lst[N % 10] * mul)
            N = N // 10
            mul = mul * 10
        else:
            return False
    return res != N_copy