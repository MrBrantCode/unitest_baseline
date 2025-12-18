"""
QUESTION:
Given an array, if ‘n’ positive integers, count the number of pairs of integers in the array that have the sum divisible by 4. 
Example 1:
Input : Arr[] = {2, 2, 1, 7, 5}
Output : 3
Explanation:
(2,2), (1,7) and(7,5) are the 3 pairs.
Example 2:
Input : Arr[] = {2, 2, 3, 5, 6}
Output : 4
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function count4Divisibiles() that takes an array (arr), sizeOfArray (n), and return the number of pairs. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ arr[] ≤ 10^{5}
"""

def count_pairs_divisible_by_4(arr, n):
    # Initialize an array to count remainders when divided by 4
    rem = [0] * 4
    
    # Count the remainders
    for index in range(n):
        rem[arr[index] % 4] += 1
    
    # Calculate the number of pairs
    ans = 0
    ans += rem[0] * (rem[0] - 1) // 2  # Pairs with remainder 0
    ans += rem[2] * (rem[2] - 1) // 2  # Pairs with remainder 2
    ans += rem[1] * rem[3]             # Pairs with remainders 1 and 3
    
    return ans