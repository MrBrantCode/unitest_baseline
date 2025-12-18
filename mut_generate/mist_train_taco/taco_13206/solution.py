"""
QUESTION:
Given an array of integers having n elements, return the numbers that occur more than floor(n/3) times in that array in increasing order. 
Example 1:
Input: arr[] = {1, 2, 1, 3, 1, 2}
Output: 1
Explanation:
Here we have 3 diffrent type of element 
1, 2 and 3. Now, You can count the frequency 
of all the elements
1 -> 3
2 -> 2
3 -> 1 
So, the only element which have frequency
greater than  ⌊n/3⌋ is {1}.
Example 2:
Input: arr[] = {1, 2, 2, 3, 2, 3, 2, 3} 
Output: 2 3
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function compute() that takes an array (arr), sizeOfArray (n), and return the array of the elements that occur more than ⌊n/3⌋ times in increasing order. The driver code automatically returns -1 in case of no elements ocuring more than ⌊n/3⌋ times.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ A[i] ≤ 10^{5}
"""

def find_elements_occurring_more_than_n_over_3_times(arr, n):
    d = {}
    res = []
    comp = n // 3
    
    for elem in arr:
        d[elem] = d.get(elem, 0) + 1
        if d[elem] > comp:
            res.append(elem)
            d[elem] = float('-inf')  # Mark as processed to avoid duplicates in result
    
    res.sort()
    return res if res else [-1]