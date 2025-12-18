"""
QUESTION:
Pulkit is really good at maths. Recently, he came to know about a problem on matrices. Amazed by the problem he got, he asked Ashish the same problem. Ashish also being good at maths solved the problem within 5 minutes. Now, its your time to solve the problem.

You will be given n*m binary matrix. You need to tell if it is possible to delete a column such that after deleting that column, rows of the matrix will be unique. If yes than print "Yes" else print "No". 

[Input]
First line contains an integer t denoting no.of test cases. 
Next line contains 2 integers n and m denoting no.of rows and columns.
Next n line contains binary string of length m each.

[Output]
For each test case output "Yes" or "No".

[Constraints]
1 ≤ t ≤ 100
1 ≤ n ≤ 1000
2 ≤ m ≤ 1000

SAMPLE INPUT
2
3 3
101
000
100
2 2
11
11

SAMPLE OUTPUT
Yes
No
"""

def can_delete_column_to_make_rows_unique(matrix, n, m):
    # Convert each row to an integer representation
    row_integers = [int(''.join(row), 2) for row in matrix]
    
    # Check if all rows are unique
    if len(set(row_integers)) == n:
        return "Yes"
    
    # Try deleting each column one by one and check if rows become unique
    for col in range(m):
        modified_rows = []
        for row in matrix:
            modified_row = row[:col] + row[col+1:]
            modified_rows.append(int(''.join(modified_row), 2))
        
        if len(set(modified_rows)) == n:
            return "Yes"
    
    return "No"