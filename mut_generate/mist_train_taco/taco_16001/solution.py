"""
QUESTION:
Find the first non-repeating element in a given array arr of N integers.
Note: Array consists of only positive and negative integers and not zero.
Example 1:
Input : arr[] = {-1, 2, -1, 3, 2}
Output : 3
Explanation:
-1 and 2 are repeating whereas 3 is 
the only number occuring once.
Hence, the output is 3. 
 
Example 2:
Input : arr[] = {1, 1, 1}
Output : 0
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function firstNonRepeating() that takes an array (arr), sizeOfArray (n), and returns the first non-repeating element. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 10^{7}
-10^{16} <= A_{^{i }}<= 10^{16}
{A_{i} !=0 }
"""

def find_first_non_repeating(arr, n):
    from collections import Counter
    
    # Create a counter dictionary to count occurrences of each element
    element_counts = Counter(arr)
    
    # Iterate through the array to find the first non-repeating element
    for element in arr:
        if element_counts[element] == 1:
            return element
    
    # If no non-repeating element is found, return 0
    return 0