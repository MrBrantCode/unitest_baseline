"""
QUESTION:
Given an array Arr of size N, the array contains numbers in range from 0 to K-1 where K is a positive integer and K <= N. Find the maximum repeating number in this array. If there are two or more maximum repeating numbers return the element having least value.
Example 1:
Input:
N = 4, K = 3
Arr[] = {2, 2, 1, 2}
Output: 2
Explanation: 2 is the most frequent
element.
Example 2:
Input:
N = 6, K = 3
Arr[] = {2, 2, 1, 0, 0, 1}
Output: 0
Explanation: 0, 1 and 2 all have same
frequency of 2.But since 0 is smallest,
you need to return 0.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxRepeating() which takes the array of integers arr, n and k as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(K)
Constraints:
1 <= N <= 10^{7}
1 <= K <= N
0 <= Arr_{i} <= K - 1
"""

def max_repeating(arr, n, k):
    freq = [0] * k
    max_count = 0
    res = -1
    
    for i in range(n):
        freq[arr[i]] += 1
        if freq[arr[i]] > max_count:
            max_count = freq[arr[i]]
            res = arr[i]
        elif freq[arr[i]] == max_count and arr[i] < res:
            res = arr[i]
    
    return res