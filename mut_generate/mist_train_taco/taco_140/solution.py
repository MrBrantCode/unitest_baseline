"""
QUESTION:
In the advanced algorithm class, n2 students sit in n rows and n columns. One day, a professor who teaches this subject comes into the class, asks the shortest student in each row to lift up his left hand, and the tallest student in each column to lift up his right hand. What is the height of the student whose both hands are up ? The student will become a target for professor’s questions.

Given the size of the class, and the height of the students in the class, you have to print the height of the student who has both his hands up in the class.



Input

The input will consist of several cases. the first line of each case will be n(0 < n < 100), the number of rows and columns in the class. It will then be followed by a n-by-n matrix, each row of the matrix appearing on a single line. Note that the elements of the matrix may not be necessarily distinct. The input will be terminated by the case n = 0.

Output

For each input case, you have to print the height of the student in the class whose both hands are up. If there is no such student, then print 0 for that case.

Example

Input

3
1 2 3
4 5 6
7 8 9
3
1 2 3
7 8 9
4 5 6
0


Output

7
7
"""

def find_target_student_height(n, students):
    if n == 0:
        return 0
    
    # Find the shortest student in each row
    s_list = [[min(row) == s for s in row] for row in students]
    
    # Find the tallest student in each column
    t_list = [[max(col) == s for s in col] for col in zip(*students)]
    
    # Find the student who has both hands up
    target_heights = []
    for (i, data) in enumerate(zip(s_list, zip(*t_list))):
        for (j, d) in enumerate(zip(*data)):
            if all(d):
                target_heights.append(students[i][j])
    
    # Return the maximum height among the target students, or 0 if no such student exists
    return max(target_heights, default=0)