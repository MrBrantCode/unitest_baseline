"""
QUESTION:
Given a non-negative number N in the form of a string.Find the largest number that can be formed by swapping two characters at most once.
 
Example 1:
Input:
N=768
Output:
867
Explanation:
Swapping the 1st and 3rd 
characters(7 and 8 respectively),
gives the largest possible number.
Example 2:
Input:
N=333
Output:
333
Explanation:
Performing any swaps gives the 
same result i.e 333.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function LargestSwap() which takes the string N as input parameter and returns the maximum possible string possible with at most one swap.
Expected Time Complexity:O(|N|)
Expected Auxillary Space:O(1)
Constraints:
1<=|N|<=10^{5}
"""

def largest_swap(N: str) -> str:
    n = len(N)
    arr = list(N)
    right = [0] * n
    right[n - 1] = n - 1
    rmax = n - 1
    
    # Fill the right array with the index of the maximum element to the right of each element
    for i in range(n - 2, -1, -1):
        right[i] = rmax
        if arr[i] > arr[rmax]:
            rmax = i
    
    # Perform the swap if it increases the value of the number
    for i in range(0, n):
        if arr[right[i]] > arr[i]:
            arr[right[i]], arr[i] = arr[i], arr[right[i]]
            break
    
    return ''.join(arr)