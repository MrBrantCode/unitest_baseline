"""
QUESTION:
Given an array Arr of N positive integers. Find the number of pairs of integers whose difference is equal to a given number K.
Note: (a, b) and (b, a) are considered same. Also, same numbers at different indices are considered different.
Example 1:
Input: 
N = 5
Arr[] = {1, 5, 3, 4, 2}
K = 3
Output: 2
Explanation: There are 2 pairs with difference 3, 
             the pairs are {1, 4} and {5, 2} 
Example 2:
Input: 
N = 6
Arr[] = {8, 12, 16, 4, 0, 20}
K = 4
Output: 5
Explanation: There are 5 pairs with difference 4, 
             the pairs are {0, 4}, {4, 8}, 
             {8, 12}, {12, 16} and {16, 20} 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countPairsWithDiffK() which takes the array arr[], n and k as inputs and returns an integer denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(max(Arr_{i}))
Constraints:
1 <= N <= 10^{5}
0 <= K <= 10^{5}
0 <= Arr_{i} <= 10^{5}
"""

def count_pairs_with_diff_k(arr, k):
    res = 0
    mapp = {}
    
    # Populate the dictionary with counts of each element
    for a in arr:
        if a not in mapp:
            mapp[a] = 1
        else:
            mapp[a] += 1
    
    # If k is 0, count pairs of the same number
    if k == 0:
        for i in sorted(mapp):
            if mapp[i] > 1:
                res += mapp[i] * (mapp[i] - 1) // 2  # Combination formula C(n, 2)
    else:
        # Count pairs with difference k
        for i in sorted(mapp):
            if i + k in mapp:
                res += mapp[i] * mapp[i + k]
    
    return res