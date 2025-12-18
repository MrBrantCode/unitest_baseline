"""
QUESTION:
Given an array A of n elements, rearrange the array according to the following relations :
 , if i is even.
 , if i is odd.[Considering 1-indexed array]
Return the resultant array.
Example:
Input 1:
A[] = {1, 2, 2, 1}
Output:
1 2 1 2
Explanation:
Both 2 are at even positions and 1 at odd satisfying 
given condition 
Input 2:
A[] = {1, 3, 2}
Output:
1 3 2
Explanation:
Here, the array is already sorted as per the conditions.
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function assign() that takes an array (arr), sizeOfArray (n), and return the resultant array.
Note: Generated output will depict whether your returned answer is correct or wrong
Expected Time Complexity: O(NLOG(N)).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ arr[i] ≤ 10^{6}
"""

def rearrange_array(arr, n):
    arr.sort()
    last = n - 1
    first = 0
    lst = [0] * n
    for i in range(n):
        if (i + 1) % 2 == 0:
            lst[i] = arr[last]
            last -= 1
        else:
            lst[i] = arr[first]
            first += 1
    return lst