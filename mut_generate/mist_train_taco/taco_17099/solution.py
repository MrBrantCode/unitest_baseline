"""
QUESTION:
Given an integer N, Chef wants to find the smallest positive integer M such that the bitwise XOR of M and M+1 is N. If no such M exists output -1.

-----Input-----
The first line of input contain an integer T denoting the number of test cases. Each of the following T lines contains an integer N for that test case.

-----Output-----
For each test case, output a single line containing the number M or -1 as described above.

-----Constraints-----
- 1 ≤ T ≤ 5000
- 1 ≤ N ≤ 230

-----Example-----
Input:
1
3

Output:
1

-----Explanation-----First Example :  M desired in the problem would be 1. As bitwise XOR of 1 and 2 is equal to 3.
"""

def find_smallest_M(N: int) -> int:
    # Precompute the list of values 2^x - 1 for x in range(1, 31)
    special_values = [2 ** x - 1 for x in range(1, 31)]
    
    # Handle specific cases
    if N == 1:
        return 2
    elif N in special_values:
        return N // 2
    else:
        return -1