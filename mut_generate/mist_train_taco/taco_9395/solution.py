"""
QUESTION:
Given a permutation of first n natural numbers as an array and an integer k. Print the lexicographically largest permutation after at most k swaps.
Example 1:
Input:
n=5
k=3
arr[] = {4, 5, 2, 1, 3}
Output: 5 4 3 2 1
Explanation: Swap 1^{st} and 2^{nd} elements: 5 4 2 1 3 
             Swap 3^{rd} and 5^{th} elements: 5 4 3 1 2 
             Swap 4^{th} and 5^{th} elements: 5 4 3 2 1 
Example 2:
Input:
n=3
k=1
arr[] = {2, 1, 3}
Output: 3 1 2
Explanation: Swap 1^{st} and 3^{re} elements: 3 1 2 
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function KswapPermutation() that takes array arr, integer n and integer k as parameters and modifies the array arr and does not return anything.
 
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
Constraints:
2 ≤ n ≤ 10^{6}
1 ≤ k ≤ n
"""

def lexicographically_largest_permutation(arr, k):
    """
    Modifies the input list `arr` to be the lexicographically largest permutation
    after at most `k` swaps.

    Parameters:
    arr (list of int): The permutation of the first `n` natural numbers.
    k (int): The maximum number of swaps allowed.

    Returns:
    None: The function modifies the input list `arr` in place.
    """
    n = len(arr)
    position_map = {value: index for index, value in enumerate(arr)}
    
    for i in range(n):
        if k == 0:
            break
        if arr[i] == n - i:
            continue
        
        # Find the position of the largest element that can be swapped
        max_value = n - i
        max_index = position_map[max_value]
        
        # Swap the elements
        arr[i], arr[max_index] = arr[max_index], arr[i]
        
        # Update the position map
        position_map[arr[i]], position_map[arr[max_index]] = i, max_index
        
        # Decrease the number of swaps left
        k -= 1