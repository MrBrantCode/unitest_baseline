"""
QUESTION:
Given an array A. Let X be an element in the array which has the maximum frequency. The task is to find the smallest sub segment of the array which also has X as the maximum frequency element.
Note: if two or more elements have the same frequency (i.e., maximum frequency) and the same sub segment size then print the sub segment which occurs first in the array.
 
Example 1:
 
Input : A[] = {1, 2, 2, 3, 1}
Output : 2 2
Explanation:
Note that there are two elements that appear two times,
1 and 2.The smallest window for 1 is whole array and
smallest window for 2 is {2, 2}.
Since window for 2 is smaller, this is our output.
Example 2:
Input : A[] = {1, 4, 3, 3, 5, 5} 
Output : 3 3 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function smallestSubsegment() that takes an array (arr), sizeOfArray (n), and return the required sub-segment of the array. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5}
"""

def find_smallest_subsegment(arr, n):
    left = dict()
    count = dict()
    mx = 0
    mn = 0
    startindex = 0
    
    for i in range(n):
        ele = arr[i]
        if ele not in count.keys():
            left[ele] = i
            count[ele] = 1
        else:
            count[ele] += 1
        
        if count[ele] > mx:
            mx = count[ele]
            mn = i - left[ele] + 1
            startindex = left[ele]
        elif count[ele] == mx and i - left[ele] + 1 < mn:
            mn = i - left[ele] + 1
            startindex = left[ele]
    
    return arr[startindex:startindex + mn]