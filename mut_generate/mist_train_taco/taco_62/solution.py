"""
QUESTION:
Little Elephant is playing a game with arrays. He is given an array A0, A1, ..., AN−1 of N integers. And then Q queries are given, each containing an integer K. He has to tell how many subarrays satisfy the condition: the function foo returns K when it is applied to the subarray.

In this problem, a subarray is defined as a sequence of continuous elements Ai, Ai+1, ..., Aj  where 0 ≤ i ≤ j ≤ N−1. The function foo, when applied to an array, returns the minimum of all the elements in the array.

For example, foo returns 5 when it is applied to the array [7, 5, 10, 7, 5, 8]. Please note that the subarrays Ai, Ai+1, ..., Aj and Ak, Ak+1, ..., Al are different if and only if i ≠ k or j ≠ l in this problem.

-----Input-----
The first line of input contains N, denoting the size of the array. The next line contains N space separated integers A0, A1, ..., AN−1, denoting the array. Then the next line contains Q, denoting the number of queries. Each query consists of one integer per line, denoting K.

-----Output-----
For each query, print the required number of subarrays.

-----Constraints-----
- 1 ≤ N ≤ 50
- 1 ≤ Ai ≤ 1000000 (106)
- 1 ≤ Q ≤ 10
- 1 ≤ K ≤ 1000000 (106)

-----Example-----
Input:
5
4 1 2 3 4
4
3
4
6
1

Output:
2
2
0
8

-----Explanation-----
Query 1. Only the two subarrays [3, 4] and [3] satisfy.
Query 2. Again only the two subarrays [4] and [4] satisfy. Please note that these subarrays (A0 and A4) are considered different.
Query 3. No subarray satisfies.
Query 4. The eight subarrays [4, 1], [4, 1, 2], [4, 1, 2, 3], [4, 1, 2, 3, 4], [1], [1, 2], [1, 2, 3] and [1, 2, 3, 4] satisfy.
"""

def count_subarrays_with_min_k(array, queries):
    n = len(array)
    cnt = {}
    
    for i in range(n):
        mn = array[i]
        for j in range(i, n):
            mn = min(mn, array[j])
            if mn in cnt:
                cnt[mn] += 1
            else:
                cnt[mn] = 1
    
    results = []
    for k in queries:
        if k in cnt:
            results.append(cnt[k])
        else:
            results.append(0)
    
    return results