"""
QUESTION:
You are given an array A of size N. The task is to find count of elements before which all the elements are smaller. First element is always counted as there is no other element before it.
 
Example 1:
Input : 
arr[] =  {10, 40, 23, 35, 50, 7}
Output : 
3
Explanation :
The elements are 10, 40 and 50.
No of elements is 3
 
Example 2:
Input : 
arr[] = {5, 4, 1}
Output : 
1
Explanation :
There is only one element 5
No of element is 1
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countElements() which takes the array arr[] and its size N as inputs and returns the Number of Elements before which no element is bigger.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A_{i} ≤ 10^{9}
"""

def count_elements_before_smaller(arr, n):
    if n == 0:
        return 0
    
    cnt = 1
    m = arr[0]
    
    for i in range(1, n):
        if m < arr[i]:
            m = arr[i]
            cnt += 1
    
    return cnt