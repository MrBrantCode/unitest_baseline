"""
QUESTION:
Given an array arr[] of N integers which may contain duplicate elements, the index of an element of this array is given to us, the task is to find the final position of this element ( for which the index is given) in the array after the stable sort is applied on the array. 
 
Example 1:
Input: N = 10, INDEX = 5
arr[]= {3, 4, 3, 5, 2, 3, 4, 3, 1, 5}
Output: 4
Explanation: Element initial index – 5 
(third 3) After sorting array by stable 
sorting algorithm,we get array as shown 
below [1(8), 2(4), 3(0), 3(2), 3(5), 3(7),
4(1), 4(6), 5(3), 5(9)] with their 
initial indices shown in parentheses next 
to them,Element's index after sorting = 4.
 
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function getIndexInSortedArray() that takes array arr, integer N, and integer index as parameters and returns the number of uneaten leaves.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{6}
"""

def get_index_in_sorted_array(arr, n, index):
    count = 0
    element = arr[index]
    
    # Count elements equal to the target element before the given index
    for i in range(index):
        if arr[i] == element:
            count += 1
    
    # Count elements less than the target element in the entire array
    for i in range(n):
        if arr[i] < element:
            count += 1
    
    return count