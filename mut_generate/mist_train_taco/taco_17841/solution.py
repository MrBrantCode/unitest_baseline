"""
QUESTION:
Given an array A of positive integers, sort the array in ascending order such that element at index K in unsorted array stays unmoved and all other elements are sorted.
 
Example 1:
Ã¢â¬â¹Input : arr[ ] = {10, 4, 11, 7, 6, 20} 
        and K = 2
Output : 4 6 11 7 10 20
Explanation:
Sort an array except an index 2 So, 
4 6 11 7 10 20 
Ã¢â¬â¹Example 2:
Input : arr[ ] = {30, 20, 10} and K = 0
Output :  30 10 20 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function sortExceptK() that takes an array (arr), sizeOfArray (n), an integer K and return he sorted array except for the element at index K. The driver code takes care of the printing.
Expected Time Complexity: O(N*LOG(N)).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}
"""

def sort_except_k(arr, k):
    # Store the element at index k
    element_at_k = arr[k]
    
    # Sort the array excluding the element at index k
    sorted_arr = sorted(arr[:k] + arr[k+1:])
    
    # Insert the element at index k back into its original position
    sorted_arr.insert(k, element_at_k)
    
    return sorted_arr