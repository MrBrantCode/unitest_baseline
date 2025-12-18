"""
QUESTION:
Golu hates odd numbers. When he learns about binary strings he wants to find out how many binary strings of given length N exist without an odd number of consecutive 1's.

For example: For N=4 1001,1010,1110,0001 are strings which contain odd number of 1's where 1100,1111 are not. Leading zeros are allowed.

This task is very difficult for Golu he asks you for your help.
Now your task is to find how many strings of given length exist without any consecutive 1's.

INPUT First line contains number of test cases T.Each test case contains length of binary string N.
OUTPUT Print number of strings without consecutive 1's. Output become large so take module with 1000000007.
Constraints
1 ≤ T ≤ 100

1 ≤ N ≤ 1000000

SAMPLE INPUT
1
2

SAMPLE OUTPUT
2

Explanation

For N=2 Binary strings are 00 , 01 , 10 , 11 and number of strings without  odd number of consecutive 1's are 2.
"""

def count_binary_strings_without_consecutive_ones(N: int) -> int:
    MOD = 1000000007
    a = [1, 1]
    
    for x in range(2, N + 1):
        a.append((a[x-1] + a[x-2]) % MOD)
    
    return a[N]