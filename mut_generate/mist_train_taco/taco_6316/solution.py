"""
QUESTION:
Ishaan is given N integers in the form of an array A. He is asked to select all of these integers in any order. For selecting every integer he gets some points. He needs to maximize those points.
For every integer he selects, he gets points equal to the value of :
the selected integer * number of integers selected before the current integer (Refer example for explanation)
Help him find the maximum points he can get provided he can select every integer exactly 1 time.
 
Example 1:
Ã¢â¬â¹Input : arr[ ] = {1, 2, 2, 4, 9}
Output : 
Explanation:
First he selects 1
Points : 1 * 0 (no integer selected before 
this), Total Points = 0
Then he selects 2
Points : 2 * 1 (1 selected before this)
Total Points = 2
Then he selects 2
Points : 2 * 2 (1,2 selected before this)
Total Points = 6
Then he selects 4
Points : 4 * 3 (1,2,2 selected before this)
Total Points = 18
Then he selects 9
Points : 9 * 4 (1,2,2,4 selected before this)
Total Points = 54
Ã¢â¬â¹Example 2:
Input : arr[ ] = {2, 2, 2, 2} 
Output :  12 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function selection() that takes an array (arr), sizeOfArray (n), and return the maximum points he can get provided. The driver code takes care of the printing.
Expected Time Complexity: O(N*LOG(N)).
Expected Auxiliary Space: O(1).
 
 
Constraints :
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5}
"""

def maximize_points(arr, n):
    arr.sort()
    res = 0
    for i in range(n):
        res += arr[i] * i
    return res