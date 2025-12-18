"""
QUESTION:
Given an array A of size N. The elements of the array consist of positive integers. You have to find the largest element with minimum frequency. 
Example 1:
Input: 
5
2 2 5 50 1
Output:
50
Explanation :
All elements are having frequency 1 except 2.
50 is the maximum element with minimum frequency.
Example 2:
Input:
4
3 3 5 5
Output:
5
Explanation:
Both 3 and 5 have the same frequency, so 5 should be returned.
User Task:
Your task is to complete the provided function LargButMinFreq(A, n) which accepts array A and n. Hence you have to return the largest element with minimum frequency.
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
Constraints:
1 <= N <= 10^{5}
1 <= A[i] <= 10^{6}
"""

def find_largest_with_min_frequency(arr, n):
    # Dictionary to store the frequency of each element
    frequency_dict = {}
    
    # Initialize minimum frequency to a large number
    min_freq = float('inf')
    
    # Initialize maximum element with minimum frequency to a small number
    max_elem = -float('inf')
    
    # Calculate the frequency of each element
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    # Find the minimum frequency
    for freq in frequency_dict.values():
        min_freq = min(min_freq, freq)
    
    # Find the largest element with the minimum frequency
    for elem, freq in frequency_dict.items():
        if freq == min_freq:
            max_elem = max(max_elem, elem)
    
    return max_elem