"""
QUESTION:
Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X. 
Example 1:
Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
1
Explanation:
The triplet {1, 4, 8} in 
the array sums up to 13.
Example 2:
Input:
n = 5, X = 10
arr[] = [1 2 4 3 6]
Output:
1
Explanation:
The triplet {1, 3, 6} in 
the array sums up to 10.
Your Task:
You don't need to read input or print anything. Your task is to complete the function find3Numbers() which takes the array arr[], the size of the array (n) and the sum (X) as inputs and returns True if there exists a triplet in the array arr[] which sums up to X and False otherwise.
Expected Time Complexity: O(n^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 10^{3}
1 ≤ A[i] ≤ 10^{5}
"""

def find_triplet_with_sum(arr, n, X):
    # Sort the array
    arr.sort()
    
    # Iterate through the array
    for i in range(n):
        # Initialize two pointers
        j = i + 1
        k = n - 1
        
        # Use two-pointer technique to find the triplet
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total == X:
                return True
            elif total > X:
                k -= 1
            else:
                j += 1
    
    # If no triplet is found, return False
    return False