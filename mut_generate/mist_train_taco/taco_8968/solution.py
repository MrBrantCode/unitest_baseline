"""
QUESTION:
Given an array of size n, a triplet (a[i], a[j], a[k]) is called a Magic Triplet if a[i] < a[j] < a[k] and i < j < k.  Count the number of magic triplets in a given array.
 
Example 1:
Input: arr = [3, 2, 1]
Output: 0
Explanation: There is no magic triplet.
Example 2:
Input: arr = [1, 2, 3, 4]
Output: 4
Explanation: Fours magic triplets are 
(1, 2, 3), (1, 2, 4), (1, 3, 4) and 
(2, 3, 4).
 
Your Task:
You don't need to read or print anything. Your task is to complete the function countTriplets() which takes the array nums[] as input parameter and returns the number of magic triplets in the array.
 
Expected Time Complexity: O(N^{2}) 
Expected Space Complexity: O(1)
 
Constraints:
1 <= length of array <= 1000
1 <= arr[i] <= 100000
"""

def count_magic_triplets(arr):
    cnt = 0
    n = len(arr)
    li = [{1: 1, 2: 0, 3: 0} for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                li[i][2] += li[j][1]
                li[i][3] += li[j][2]
        cnt = cnt + li[i][3]
    return cnt