"""
QUESTION:
Sachin always wanted to score more and more runs for his team. Sometimes he succeeds in doing that and sometimes he fails. He also has a habit of noting down the runs he scored after every match in his diary. After N  matches he always looks for his scores. In i-th match, he scores A[i] runs. Now he wanted to know the length of the maximum non-decreasing sub-segment in sequence A. As he wants to go for another match, help him in doing this task.
Example 1:
Input:                  
N = 6                       
A[] = {2, 2, 1, 3, 4, 1}
Output:
3
Explanation:
The maximum non-decreasing sub-segment is
the segment with numbers from the third to
the fifth one.
Example 2:
Input:
N = 3
A[] = {2, 2, 9}
Output:
3
Explanation:
The maximum non-decreasing sub-segment
is the numbers from the first to the third one.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function compute() which takes the array A[] and its size N as inputs and returns the length of the maximum non-decreasing sub-segment.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤10^{5}
1 ≤ A[i] ≤ 10^{9}
"""

def max_non_decreasing_subsegment_length(A, N):
    if N == 0:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, N):
        if A[i] >= A[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    
    max_length = max(max_length, current_length)
    return max_length