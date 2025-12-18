"""
QUESTION:
Given an array of integers, sort the array according to frequency of elements. That is elements that have higher frequency come first. If frequencies of two elements are same, then smaller number comes first.
Example 1:
Input:
N = 5
A[] = {5,5,4,6,4}
Output: 4 4 5 5 6
Explanation: The highest frequency here is
2. Both 5 and 4 have that frequency. Now
since the frequencies are same then 
smallerelement comes first. So 4 4 comes 
firstthen comes 5 5. Finally comes 6.
The output is 4 4 5 5 6.
Example 2:
Input:
N = 5
A[] = {9,9,9,2,5}
Output: 9 9 9 2 5
Explanation: The highest frequency here is
3. The element 9 has the highest frequency
So 9 9 9 comes first. Now both 2 and 5
have same frequency. So we print smaller
element first.
The output is 9 9 9 2 5.
Your Task:
You only need to complete the function sortByFreq that takes arr, and n as parameters and returns the sorted array.
Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N). 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A_{i} ≤ 10^{5}
"""

import heapq

def sort_by_frequency(arr, n):
    # Step 1: Create a frequency map
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Step 2: Create a min-heap based on frequency and value
    min_heap = []
    for val, freq in freq_map.items():
        heapq.heappush(min_heap, (-freq, val))
    
    # Step 3: Sort the heap by frequency (negative) and value
    min_heap.sort(key=lambda x: (x[0], x[1]))
    
    # Step 4: Generate the sorted array based on the heap
    ans = [val for (freq, val) in min_heap for i in range(-freq)]
    
    return ans