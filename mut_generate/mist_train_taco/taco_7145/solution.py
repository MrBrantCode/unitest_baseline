"""
QUESTION:
You are given an array arr[] of n integers and q queries in an array queries[] of length 2*q containing l, r pair for all q queries. You need to compute the following sum over q queries.
 
Array is 0-Indexed.
Example 1:
Input: n = 4
arr = {1, 2, 3, 4}
q = 2
queries = {1, 4, 2, 3}
Output: 10 5
Explaination: In the first query we need sum 
from 1 to 4 which is 1+2+3+4 = 10. In the 
second query we need sum from 2 to 3 which is 
2 + 3 = 5.
Your Task:
You do not need to read input or print anything. Your task is to complete the function querySum() which takes n, arr, q and queries as input parameters and returns the answer for all the queries.
Expected Time Complexity: O(n+q)
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ n, q ≤ 1000
1 ≤ arr_{i} ≤ 10^{6}
1 ≤ l ≤ r ≤ n
"""

def query_sum(n, arr, q, queries):
    return [sum(arr[queries[i] - 1:queries[i + 1]]) for i in range(0, 2 * q, 2)]