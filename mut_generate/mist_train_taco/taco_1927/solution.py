"""
QUESTION:
Let a and b be two arrays of lengths n and m, respectively, with no elements in common. We can define a new array merge(a,b) of length n+m recursively as follows:

  * If one of the arrays is empty, the result is the other array. That is, merge(∅,b)=b and merge(a,∅)=a. In particular, merge(∅,∅)=∅. 
  * If both arrays are non-empty, and a_1<b_1, then merge(a,b)=[a_1]+merge([a_2,…,a_n],b). That is, we delete the first element a_1 of a, merge the remaining arrays, then add a_1 to the beginning of the result. 
  * If both arrays are non-empty, and a_1>b_1, then merge(a,b)=[b_1]+merge(a,[b_2,…,b_m]). That is, we delete the first element b_1 of b, merge the remaining arrays, then add b_1 to the beginning of the result. 



This algorithm has the nice property that if a and b are sorted, then merge(a,b) will also be sorted. For example, it is used as a subroutine in merge-sort. For this problem, however, we will consider the same procedure acting on non-sorted arrays as well. For example, if a=[3,1] and b=[2,4], then merge(a,b)=[2,3,1,4].

A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order. For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

There is a permutation p of length 2n. Determine if there exist two arrays a and b, each of length n and with no elements in common, so that p=merge(a,b).

Input

The first line contains a single integer t (1≤ t≤ 1000) — the number of test cases. Next 2t lines contain descriptions of test cases. 

The first line of each test case contains a single integer n (1≤ n≤ 2000).

The second line of each test case contains 2n integers p_1,…,p_{2n} (1≤ p_i≤ 2n). It is guaranteed that p is a permutation.

It is guaranteed that the sum of n across all test cases does not exceed 2000.

Output

For each test case, output "YES" if there exist arrays a, b, each of length n and with no common elements, so that p=merge(a,b). Otherwise, output "NO".

Example

Input


6
2
2 3 1 4
2
3 1 2 4
4
3 2 6 1 5 7 8 4
3
1 2 3 4 5 6
4
6 1 3 7 4 5 8 2
6
4 3 2 5 1 11 9 12 8 6 10 7


Output


YES
NO
YES
YES
NO
NO

Note

In the first test case, [2,3,1,4]=merge([3,1],[2,4]).

In the second test case, we can show that [3,1,2,4] is not the merge of two arrays of length 2.

In the third test case, [3,2,6,1,5,7,8,4]=merge([3,2,8,4],[6,1,5,7]).

In the fourth test case, [1,2,3,4,5,6]=merge([1,3,6],[2,4,5]), for example.
"""

def can_be_merged(n, p):
    def isSubsetSum(set, n, sum):
        subset = [[False for i in range(sum + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            subset[i][0] = True
        for i in range(1, sum + 1):
            subset[0][i] = False
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j < set[i - 1]:
                    subset[i][j] = subset[i - 1][j]
                if j >= set[i - 1]:
                    subset[i][j] = subset[i - 1][j] or subset[i - 1][j - set[i - 1]]
        return subset[n][sum]
    
    k = 0
    l = 0
    z = 0
    a = []
    for i in range(2 * n):
        if p[i] > l:
            z = max(k, z)
            l = p[i]
            a.append(k)
            k = 0
        k += 1
    a.append(k)
    
    if z > n or k > n:
        return False
    else:
        p_len = len(a)
        return isSubsetSum(a, p_len, n)