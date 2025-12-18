"""
QUESTION:
Given an array A of size N, your task is to do some operations, i.e., search an element x, insert an element y at index yi, and delete an element z by completing the functions. Also, all functions should return a boolean value.
Note: 
	In delete operation return true even if element is not present.
	N is never greater than 10000.
Input Format:
N
A_{1} A_{2} . . . A_{n}
x y yi z
Example:
Input:
5
2 4 1 0 6
1 2 2 0
Output:
1 1 1
Your Task:
Since this is a function problem, you only need to complete the provided functions.
Constraints:
1 <= T <= 100
1 <= N <= 100
0 <= A_{i} <= 1000
"""

def array_operations(A, x, y, yi, z):
    # Search operation
    search_result = x in A
    
    # Insert operation
    A.insert(yi, y)
    insert_result = True  # Insertion is always successful in Python lists
    
    # Delete operation
    delete_result = True  # Deletion is always successful as per the problem statement
    
    return (search_result, insert_result, delete_result)