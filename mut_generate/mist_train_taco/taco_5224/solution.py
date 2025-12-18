"""
QUESTION:
Given an array arr[] of size N and an element k. The task is to find all elements in array that appear more than n/k times.
Example 1:
Input:
N = 8
arr[] = {3,1,2,2,1,2,3,3}
k = 4
Output: 2
Explanation: In the given array, 3 and
 2 are the only elements that appears 
more than n/k times.
Example 2:
Input:
N = 4
arr[] = {2,3,3,2}
k = 3
Output: 2
Explanation: In the given array, 3 and 2 
are the only elements that appears more 
than n/k times. So the count of elements 
are 2.
Your Task:
The task is to complete the function countOccurence() which returns count of elements with more than n/k times appearance.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 10^{4}
1 <= a[i] <= 10^{6}
1 <= k <= N
"""

def count_elements_more_than_n_k(arr, n, k):
    x = n / k
    count = 0
    frequency = {}
    
    # Count the frequency of each element
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Count elements that appear more than n/k times
    for key in frequency:
        if frequency[key] > x:
            count += 1
    
    return count