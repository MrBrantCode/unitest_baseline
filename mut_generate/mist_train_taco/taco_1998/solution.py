"""
QUESTION:
Given an array, Arr of N numbers, and another number target, find three integers in the array such that the sum is closest to the target. Return the sum of the three integers.
Note: If there are multiple solutions, print the maximum one.
Example 1:
Input:
N = 6, target = 2
A[] = {-7,9,8,3,1,1}
Output: 2
Explanation: There is one triplet with sum
2 in the array. Triplet elements are -7,8,
1 whose sum is 2.
Example 2:
Input:
N = 4, target = 13
A[] = {5,2,7,5}
Output: 14
Explanation: There is one triplet with sum
12 and other with sum 14 in the array.
Triplet elements are 5, 2, 5 and 2, 7, 5
respectively. Since abs(13-12) ==
abs(13-14) maximum triplet sum will be
preferred i.e 14.
Your Task:
Complete threeSumClosest() function and return the expected answer.
Expected Time Complexity: O(N*N).
Expected Auxiliary Space: O(1).
Constraints:
3 ≤ N ≤ 10^{3}
-10^{5} ≤ A[i] ≤ 10^{5}
1 ≤ target ≤ 10^{5}
"""

def find_closest_triplet_sum(arr, target):
    arr.sort()
    closest_sum = sum(arr[:3])
    
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            elif abs(target - current_sum) == abs(target - closest_sum):
                closest_sum = max(closest_sum, current_sum)
            
            if current_sum < target:
                left += 1
            else:
                right -= 1
    
    return closest_sum