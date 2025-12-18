"""
QUESTION:
Given an array arr[], count number of pairs arr[i], arr[j] such that arr[i] + arr[j] is maximum and i < j.
Example 1:
Input : Arr[] = {1, 1, 1, 2, 2, 2}
Output : 3
Explanation:
We have an array [1, 1, 1, 2, 2, 2]
The maximum possible pair
sum where i is less than j is  4, which 
is given by 3 pairs, so the answer is 3
the pairs are (2, 2), (2, 2) and (2, 2).
Example 2:
Input : Arr[] = {1, 4, 3, 3, 5, 1}
Output : 1
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function MaximumSum() that takes an array (arr), sizeOfArray (n), and return the number of pairs whose sum is maximum. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
CONSTRAINTS:
1 ≤ a[i], n ≤ 10^{5}
"""

from collections import defaultdict

def count_max_sum_pairs(arr, n):
    if n == 1:
        return 0
    
    store = defaultdict(int)
    for item in arr:
        store[item] += 1
    
    maxi = max(store.keys())
    if store[maxi] > 1:
        return store[maxi] * (store[maxi] - 1) // 2
    
    del store[maxi]
    return store[max(store.keys())]