"""
QUESTION:
Given an unsorted array of integers and a sum. The task is to count the number of subarray which adds to the given sum.
Example 1:
Input:
n = 5
arr[] = {10,2,-2,-20,10}
sum = -10
Output: 3
Explanation: Subarrays with sum -10 are: 
[10, 2, -2, -20], [2, -2, -20, 10] and 
[-20, 10].
Example 2:
Input:
n = 6
arr[] = {1,4,20,3,10,5}
sum = 33
Output: 1
Explanation: Subarray with sum 33 is: 
[20,3,10].
Your Task:
This is a function problem. You only need to complete the function subArraySum() that takes arr, n, sum as parameters and returns the count of subarrays which adds up to the given sum. 
Expected Time Comlexity: O(n)
Expected Auxilary Space: O(n)
Constraints:
1 <= n <= 10^{5}
-10^{5} <= arr[i] <= 10^{5}
-10^{5} <= sum <= 10^{5}
"""

def count_subarrays_with_sum(arr, sum_value):
    """
    Counts the number of subarrays that sum up to the given sum_value.

    Parameters:
    arr (list of int): The input array of integers.
    sum_value (int): The target sum for the subarrays.

    Returns:
    int: The count of subarrays that sum up to sum_value.
    """
    d = {}
    mysum = 0
    count = 0
    
    for num in arr:
        mysum += num
        
        if mysum == sum_value:
            count += 1
        
        if (mysum - sum_value) in d:
            count += d[mysum - sum_value]
        
        if mysum in d:
            d[mysum] += 1
        else:
            d[mysum] = 1
    
    return count