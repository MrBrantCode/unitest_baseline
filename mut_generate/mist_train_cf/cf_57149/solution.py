"""
QUESTION:
Given the array `arr` of positive integers and the array `queries` where `queries[i] = [Li, Ri, Ki]`, implement the function `solve(arr, queries)` to compute the XOR of elements from `Li` to `Ri` in `arr` (inclusive), then XOR the result with `Ki` for each query `i`. Return an array containing the results for all queries. Constraints: `1 <= arr.length <= 3 * 10^4`, `1 <= arr[i] <= 10^9`, `1 <= queries.length <= 3 * 10^4`, `queries[i].length == 3`, `0 <= queries[i][0] <= queries[i][1] < arr.length`, `0 <= queries[i][2] <= 10^9`.
"""

def xorQueries(arr, queries):
    prefix = [0]
    for num in arr:
        prefix.append(prefix[-1] ^ num)
        
    ans = []
    for L, R, K in queries:
        ans.append(prefix[R + 1] ^ prefix[L] ^ K)
    return ans