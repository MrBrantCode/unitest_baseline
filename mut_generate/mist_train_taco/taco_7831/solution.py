"""
QUESTION:
There is a class of N students and the task is to find the top K marks scorers. You need to print the index of the toppers of the class which will be same as the index of the student in the input array (use 0-based indexing). First print the index of the students having highest marks then the students with second highest and so on. If there are more than one students having same marks then print their indices in ascending order.Suppose k = 2 and the students having highest marks have indices 0 and 5 and students having second highest marks have indices 6 and 7 then output will be 0 5 6 7.
Example 1:
Input:
N=5 K=3
arr[] = { 2, 2, 1, 3, 1 }
Output: 3 0 1 2 4
Explanation: Topper with 3 marks is present 
at 3rd index, 2 marks is present at 0^{th} 
index and next at 1^{st} index. 1 marks is present 
at 2 and 4.
Example 2:
Input:
N=4 K=1
arr[] = { 1, 2, 3, 4 } 
Output: 3
Explanation: The highest marks is at index 3.
Your Task:
Since this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function kTop() that takes array A and integer N as parameters and change the given array according to the given conditions. You do not have to return anything
 
Expected Time Complexity: O(NlogN).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{6}
1 ≤ M ≤ 10^{6}
"""

def find_top_k_indices(arr, N, K):
    # Create a list of tuples where each tuple is (marks, index)
    indexed_marks = [(arr[i], i) for i in range(N)]
    
    # Sort the list of tuples first by marks in descending order, then by index in ascending order
    indexed_marks.sort(key=lambda x: (-x[0], x[1]))
    
    # Extract the indices of the top K marks scorers
    top_k_indices = [indexed_marks[i][1] for i in range(K)]
    
    return top_k_indices