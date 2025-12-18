"""
QUESTION:
You are provided with marks of N students in Physics, Chemistry and Maths.
Perform the following 3 operations: 
	Sort the students in Ascending order of their Physics marks.
	Once this is done, sort the students having same marks in Physics in the descending order of their Chemistry marks.
	Once this is also done, sort the students having same marks in Physics and Chemistry in the ascending order of their Maths marks.
Example 1:
Input:
N = 10
phy[] = {4 1 10 4 4 4 1 10 1 10}
chem[] = {5 2 9 6 3 10 2 9 14 10}
math[] = {12 3 6 5 2 10 16 32 10 4}
Output:
1 14 10
1 2 3
1 2 16
4 10 10
4 6 5
4 5 12
4 3 2
10 10 4
10 9 6
10 9 32
Explanation: Firstly, the Physics marks of 
students are sorted in ascending order.
Those having same marks in Physics have
their Chemistry marks in descending order.
Those having same marks in both Physics
and Chemistry have their Math marks in
ascending order.
Your Task:
You don't need to read input or print anything. Your task is to complete the function customSort() which takes  phy[],  chem[],  math[]  and an integer N denoting the marks and the number of students. The function sorts the marks in the described order and the final changes should be made in the given arrays only.
Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 10000
"""

def custom_sort(phy, chem, math, N):
    # Combine the marks into a list of tuples
    marks = [(phy[i], chem[i], math[i]) for i in range(N)]
    
    # Sort the list of tuples based on the specified criteria
    marks.sort(key=lambda x: (x[0], -x[1], x[2]))
    
    # Update the original lists with the sorted values
    for i in range(N):
        phy[i], chem[i], math[i] = marks[i]