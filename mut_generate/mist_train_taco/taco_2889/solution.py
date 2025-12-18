"""
QUESTION:
Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.The result is going to be very large, hence return the result in the form of a string.
Example 1:
Input: 
N = 5
Arr[] = {3, 30, 34, 5, 9}
Output: 9534330
Explanation: Given numbers are {3, 30, 34,
5, 9}, the arrangement 9534330 gives the
largest value.
Example 2:
Input: 
N = 4
Arr[] = {54, 546, 548, 60}
Output: 6054854654
Explanation: Given numbers are {54, 546,
548, 60}, the arrangement 6054854654 
gives the largest value.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function printLargest() which takes the array of strings arr[] as parameter and returns a string denoting the answer.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ Arr[i] ≤ 10^{18}
Sum of all the elements of the array is greater than 0.
"""

import functools

def form_largest_number(arr):
    """
    Form the largest possible number by arranging the given non-negative integers.

    Parameters:
    arr (list of int): A list of non-negative integers.

    Returns:
    str: The largest possible number that can be formed as a string.
    """
    
    # Convert all numbers to strings for comparison
    arr = list(map(str, arr))
    
    # Define a custom comparator function
    def compare(x, y):
        if x + y > y + x:
            return -1
        else:
            return 1
    
    # Sort the array using the custom comparator
    arr.sort(key=functools.cmp_to_key(compare))
    
    # Join the sorted array to form the largest number
    return ''.join(arr)