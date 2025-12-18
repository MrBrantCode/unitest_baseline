"""
QUESTION:
Given an array arr of size N consisting of non-negative integers. You are also given Q queries represented by 2D integer array queries, where queries[ i ] = [xi, mi].
The answer to the i^{th} query is the maximum bitwise XOR value of x_{i} and any element of arr that does not exceed m_{i}. In other words, the answer is max(arr [ j ] XOR x_{i}) for all j such that arr [ j ] <= m_{i} . If all elements in nums are larger than mi , then answer is -1.
Return an integer array answer where answer [ i ] is the answer to the i^{th} query.
Example 1:
Input:
N = 5
Q = 3
arr [ ] = {0, 1, 2, 3, 4}
queries [ ][ ] = {{3, 1}, {1, 3}, {5, 6}}
Output: {3, 3, 7}
Explanation: 
1.  0 and 1 are the only two integers not greater than 1. 
0 XOR 3 = 3 and 1 XOR 3 = 2.
The larger of the two is 3.
2.  1 XOR 2 = 3.
3.  5 XOR 2 = 7.
Example 2:
Input:
N = 6
Q = 3
arr [ ] = {5, 2, 4, 6, 6, 3}
queries [ ][ ] = {{12, 4}, {8, 1}, {6, 3}}
Output: {15, -1, 5}
Your Task:
You don't need to read input or print anything. Your task is to complete the function maximumXor() which takes the interger N, integer Q, integer array arr [ ] and 2D integer array queries [ ][ ]  as parameters and returns integer array where, the i^{th} element is the answer to the ith query.
Expected Time Complexity: O(max(QlogQ, NlogN))
Expected Auxiliary Space: O(Q + N)
Constraints:
1 ≤ N, Q ≤ 10^{5}
0 ≤ arr_{i} , x_{i} , m_{i} ≤ 10^{9}
"""

from bisect import bisect_left, bisect_right

def maximum_xor(N, Q, arr, queries):
    arr.sort()
    answer = []
    for (x, m) in queries:
        (start, stop) = (0, bisect_right(arr, m))
        num = 0
        for i in range(30)[::-1]:
            cut = bisect_left(arr, num + (1 << i), start, stop)
            if cut > start and x & 1 << i:
                stop = cut
            elif cut < stop:
                start = cut
                num += 1 << i
        answer.append(num ^ x if start < stop else -1)
    return answer