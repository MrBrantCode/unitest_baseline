"""
QUESTION:
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.


Formally the function should:
Return true if there exists i, j, k  
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 
else return false.



Your algorithm should run in O(n) time complexity and O(1) space complexity.


Examples:
Given [1, 2, 3, 4, 5],
return true.


Given [5, 4, 3, 2, 1],
return false.


Credits:Special thanks to @DjangoUnchained for adding this problem and creating all test cases.
"""

def has_increasing_triplet(nums: list[int]) -> bool:
    n1 = n2 = float('inf')
    for n in nums:
        if n <= n1:
            n1 = n
        elif n <= n2:
            n2 = n
        else:
            return True
    return False