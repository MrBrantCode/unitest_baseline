"""
QUESTION:
Given an array of n integers. Find the kth distinct element.
Example 1:
Input: 
n = 6, k = 2
arr = {1, 2, 1, 3, 4, 2}
Output:
4
Explanation: 1st distinct element will be 3
and the 2nd distinct element will be 4. As 
both the elements present in the array only 1 
times.
Example 2:
Input: 
n = 6, k = 3
arr = {1, 2, 50, 10, 20, 2}
Output:
10
Your Task:
You don't need to read or print anything. Your task is to complete the function KthDistinct() which takes the array of elements as input parameter and returns the kth distinct element. If not possible return -1.
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
Constranits:
1 <= length of array <= 10^{5}
1 <= elements of array <= 10^{6}
"""

def find_kth_distinct_element(arr, k):
    # Dictionary to count the frequency of each element
    frequency_dict = {}
    
    # Count the frequency of each element in the array
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    # Find the kth distinct element
    distinct_count = 0
    for num in arr:
        if frequency_dict[num] == 1:
            distinct_count += 1
            if distinct_count == k:
                return num
    
    # If kth distinct element is not found, return -1
    return -1