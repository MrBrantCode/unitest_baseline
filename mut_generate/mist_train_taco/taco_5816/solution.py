"""
QUESTION:
As a programmer, it is very necessary to maintain balance in the life.
Here is task for you to maintain a balance. Your task is to find whether a given number x is balanced with respect to a given array a[ ] which is sorted in non-decreasing order.
Given a sorted array a[ ], the ceiling of x is the smallest element in the array greater than or equal to x, and the floor of x is the greatest element smaller than or equal to x. The number 'x' is said to be balanced if the absolute difference between floor of x and x is equal to the absolute difference between ceil of x and x i.e. if absolute(x - floor(x, a[])) = absolute(ceil(x, a[]) - x).
If one of floor or ceil does not exist assume 'x' to be balanced.
Example 1:
Input:
N = 7  
x = 5
a[] = {1, 2, 8, 10, 10, 12, 19} 
Output: 
Balanced
Explanation: Here 2 is the floor value and 
8 is the ceil value and (5 - 2) = (8 - 5).  
Example 2:
Input:
N = 8  
x = 9 
a[] = {1, 2, 5, 7, 8, 11, 12, 15} 
Output: 
Not Balanced
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function FindElement() that takes array a[ ], its size N and integer x as input parameters and returns the string "Balanced" if the absolute difference between floor of x and x is equal to the absolute difference between ceil of x and x or else returns string "Not Balanced".
Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{6}
"""

def is_balanced(arr, n, x):
    # Initialize the start and end pointers for binary search
    s = 0
    e = n - 1
    
    # Perform binary search to find the floor and ceil of x
    while s <= e:
        mid = (s + e) // 2
        
        # Check if the current mid element is the ceil of x
        if arr[mid] >= x:
            e = mid - 1
        else:
            s = mid + 1
    
    # Determine the floor and ceil values
    floor = arr[e] if e >= 0 else None
    ceil = arr[s] if s < n else None
    
    # Check if x is balanced
    if floor is None or ceil is None:
        return "Balanced"
    elif abs(x - floor) == abs(ceil - x):
        return "Balanced"
    else:
        return "Not Balanced"