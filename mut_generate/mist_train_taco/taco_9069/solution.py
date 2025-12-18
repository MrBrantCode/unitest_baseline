"""
QUESTION:
Given the marks of N students in an Array A, calculate the mean.
Note: If result is a Decimal Value, find it's floor Value. 
Example 1:
Input:
N = 4 
A = { 56 , 67 , 30 , 79 }
Output:
58
Explanation:
56+67+30+79 = 232;  232/4 = 58.
So, the Output is 58.
Example 2:
Input:
N = 4 
A = { 78 , 89 , 67 , 76 }
Output:
77
Explanation:
78+89+67+76  = 310;  310/4 = 77.5 = 77.
So, the Output is 77.
Your Task:
You don't need to read input or print anything. Your task is to complete the function mean() which takes 1 Integer N and an Array A as input and returns the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{4}
1 <= A[i] <= 10^{4}
"""

def calculate_mean(N, A):
    """
    Calculate the floor value of the mean of the marks of N students.

    Parameters:
    N (int): The number of students.
    A (list of int): The list of marks of the students.

    Returns:
    int: The floor value of the mean of the marks.
    """
    if N != len(A):
        raise ValueError("The length of the array A must be equal to N.")
    
    mean_value = sum(A) / N
    return int(mean_value)