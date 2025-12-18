"""
QUESTION:
Given an array Arr[] of N distinct integers. Write a program to find the count of groups of 2 or 3 integers that can be formed by choosing integers from the given array such that sum of integers in each of the group is divisible by three.
 
Example 1:
Input:
N = 4
Arr[] = {1, 2, 3, 5}
Output:
4
Explanation:
There are only 4 possible groups: (1,2,3);
(1,2) ; (1,5) ; (1,3,5)
Example 2:
Input:
N = 3
Arr[] = {1, 1, 1}
Output:
1
Explanation:
There is only 1 possible group: (1,1,1).
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function noOfGroups() which takes an Integer N and an array Arr as input and returns the answer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{5}
1 <= Arr[i] <= 10^{5}
"""

def count_groups_divisible_by_three(arr, n):
    c = [0, 0, 0]
    res = 0
    
    # Count the number of elements that give remainder 0, 1, and 2 when divided by 3
    for i in range(n):
        c[arr[i] % 3] += 1
    
    # Calculate the number of groups of 2 or 3 whose sum is divisible by 3
    res += (c[0] * (c[0] - 1)) // 2
    res += c[1] * c[2]
    res += (c[0] * (c[0] - 1) * (c[0] - 2)) // 6
    res += (c[1] * (c[1] - 1) * (c[1] - 2)) // 6
    res += (c[2] * (c[2] - 1) * (c[2] - 2)) // 6
    res += c[0] * c[1] * c[2]
    
    return res