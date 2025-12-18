"""
QUESTION:
Given a sorted array arr[ ] of N positive integers. Your task is to find an index i in the array from where the number of elements smaller than arr[i] in the left side of the index is equal to the number of elements greater than arr[i] in the right side of the index.
If no such index exists, print "-1".
Example 1:
Input:
N = 6
arr[] = {1, 2, 3, 3, 3, 3}
Output:
1
Explanation:
2 is the element before which we have one
element that is smaller than 2 and we have
one element to its right which is greater
than 2. Hence, print the index of 2.
Example 2:
Input:
N = 8
arr[] = {1, 2, 3, 3, 3, 3, 4, 4}
Output:
-1
Explanation:
There is no index as such, so print -1
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findEqualPoint() which takes the array arr[] and its size N as input parameters and returns the required index. If there are multiple indices, return the smallest one. If such index doesn't exist then return "-1" (without quotes).
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A_{i} ≤ 10^{12}
"""

def find_equal_point(arr: list[int], n: int) -> int:
    """
    Finds an index i in the sorted array arr where the number of elements smaller than arr[i] 
    on the left side is equal to the number of elements greater than arr[i] on the right side.
    
    Parameters:
    arr (list[int]): A sorted array of positive integers.
    n (int): The size of the array.
    
    Returns:
    int: The index i where the condition is satisfied. If no such index exists, returns -1.
    """
    if n == 1:
        return 0
    
    mini = [0] * n
    maxi = [0] * n
    
    # Fill maxi array
    for j in range(n - 2, -1, -1):
        if arr[j] == arr[j + 1]:
            maxi[j] = maxi[j + 1]
        else:
            maxi[j] = maxi[j + 1] + 1
    
    # Fill mini array and check condition
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            mini[i] = mini[i - 1]
        else:
            mini[i] = mini[i - 1] + 1
        
        if mini[i] == maxi[i]:
            return i
    
    return -1