"""
QUESTION:
Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
Note: Array should start with a positive number and 0 (zero) should be considered a positive element.
 
Example 1:
Input: 
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Explanation : Positive elements : 9,4,5,0,2
Negative elements : -2,-1,-5,-3
As we need to maintain the relative order of
postive elements and negative elements we will pick
each element from the positive and negative and will
store them. If any of the positive and negative numbers
are completed. we will continue with the remaining signed
elements.The output is 9,-2,4,-1,5,-5,0,-3,2.
Example 2:
Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
Explanation : Positive elements : 5,2,4,7,1,8,0
Negative elements : -5,-2,-8
As we need to maintain the relative order of
postive elements and negative elements we will pick
each element from the positive and negative and will
store them. If any of the positive and negative numbers
are completed. we will continue with the remaining signed
elements.The output is 5,-5,2,-2,4,-8,7,1,8,0.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function rearrange() which takes the array of integers arr[] and n as parameters. You need to modify the array itself.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{7}
-10^{6} ≤ Arr[i] ≤ 10^{7}
"""

def rearrange_array(arr, n):
    """
    Rearranges the elements of the array such that positive and negative numbers
    alternate while maintaining their relative order. The array starts with a positive number.

    Parameters:
    arr (list of int): The input array containing positive and negative integers.
    n (int): The size of the array.

    Returns:
    None: The function modifies the input array in place.
    """
    pn = []  # List to store positive numbers
    nn = []  # List to store negative numbers
    
    # Separate positive and negative numbers
    for i in arr:
        if i < 0:
            nn.append(i)
        else:
            pn.append(i)
    
    i = 0
    pn.reverse()  # Reverse to use pop() efficiently
    nn.reverse()  # Reverse to use pop() efficiently
    
    # Alternate positive and negative numbers
    while len(pn) != 0 and len(nn) != 0:
        p = pn.pop()
        arr[i] = p
        i += 1
        n = nn.pop()
        arr[i] = n
        i += 1
    
    # If there are remaining positive numbers
    if len(pn) != 0:
        while len(pn) > 0:
            p = pn.pop()
            arr[i] = p
            i += 1
    
    # If there are remaining negative numbers
    if len(nn) != 0:
        while len(nn) > 0:
            n = nn.pop()
            arr[i] = n
            i += 1