"""
QUESTION:
Given a function that takes a binary string. The task is to return the longest size of contiguous substring containing only ‘1’.
Input:
The first line of input contains an integer T denoting the no of test cases.Then T test cases follow. Each test case contains a string S.
Output:
For each test case return the maximum length of required sub string.
Constraints: 
1<=T<=100
1<=|string length|<=10^{4}
Example:
Input:
2
110
11101110
Output:
2
3
"""

def longest_contiguous_ones(binary_string: str) -> int:
    count = 0
    max_length = 0
    
    for char in binary_string:
        if char == '1':
            count += 1
            if count > max_length:
                max_length = count
        else:
            count = 0
    
    return max_length