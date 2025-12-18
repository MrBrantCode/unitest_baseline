"""
QUESTION:
Given an array of size n, Find the subarray with least average of size k.
 
Example 1:
Input: nums = [30, 20, 10], k = 1
Output: 3
Explanation: Subarrays of length 1 are
{30}, {20}, {10}. {10} has the least 
average.
Example 2:
Input: nums = [30, 20, 10], k = 2
Output: 2
Explanation: Subarrays of length 2 are
{30, 20}, {20, 10}. {20, 10} has the least 
average.
 
Your Task:
You don't need to read or print anything. Yous task is to complete the function least_average() which takes the array and k as input parameter and returns the index of the first element of the subarray(1-based indexing) of size k that has least average.
 
Expected Time Complexity: O(n)
Expected Space Compelxity: O(1)
 
Constraints:
1 <= k <= n <= 100000
1 <= elements of array <= 1000000
"""

def find_subarray_with_least_average(nums, k):
    minAvg = 0
    avg = 0
    index = 1
    n = len(nums)
    
    # Calculate the initial average of the first subarray of size k
    for i in range(k):
        avg += nums[i]
    avg /= k
    minAvg = avg
    
    # Iterate through the array to find the subarray with the least average
    for i in range(1, n - k + 1):
        avg = (avg * k - nums[i - 1] + nums[i + k - 1]) / k
        if minAvg > avg:
            minAvg = avg
            index = i + 1
    
    return index