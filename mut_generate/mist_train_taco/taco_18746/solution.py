"""
QUESTION:
Given an array of integers, your task is to find the smallest and second smallest element in the array. If smallest and second smallest do not exist, print -1.
Example 1:
Input :
5
2 4 3 5 6
Output :
2 3 
Explanation: 
2 and 3 are respectively the smallest 
and second smallest elements in the array.
Example 2:
Input :
6
1 2 1 3 6 7
Output :
1 2 
Explanation: 
1 and 2 are respectively the smallest 
and second smallest elements in the array.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minAnd2ndMin() which takes the array A[] and its size N as inputs and returns a vector containing the smallest and second smallest element if possible, else return {-1,-1}.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1<=N<=10^{5}
1<=A[i]<=10^{5}
"""

def find_smallest_and_second_smallest(arr, n):
    # Convert the array to a set to remove duplicates and then back to a list
    arr = list(set(arr))
    
    # Sort the array
    arr.sort()
    
    # Get the first two elements of the sorted array
    smallest_elements = arr[:2]
    
    # Check if we have at least two elements
    if len(smallest_elements) == 2:
        return tuple(smallest_elements)
    else:
        return (-1, -1)