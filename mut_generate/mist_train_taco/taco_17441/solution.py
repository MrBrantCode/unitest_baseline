"""
QUESTION:
Given an array Arr of N integers that contains odd number of occurrences for all numbers except for a few elements which are present even number of times. Find the elements which have even occurrences in the array.
Example 1:
Input:
N = 11
Arr[] = {9, 12, 23, 10, 12, 12, 
15, 23, 14, 12, 15}
Output: 12 15 23
Example 2:
Input:
N = 5
Arr[] = {23, 12, 56, 34, 32}
Output: -1
Explanation: Every integer is present odd 
number of times.
Your Task:
You don't need to read input or print anything. Your task is to complete the function repeatingEven() which takes the array of integers arr and its size n as input parameters and returns a sorted array denoting the answer. If no such even occuring element is present return -1.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ Arr[i] ≤ 63
"""

from collections import Counter

def find_even_occurrences(arr, n):
    if len(set(arr)) == n:
        return [-1]
    
    count = Counter(arr)
    even_occurrences = [key for key, value in count.items() if value % 2 == 0]
    even_occurrences.sort()
    
    return even_occurrences if even_occurrences else [-1]