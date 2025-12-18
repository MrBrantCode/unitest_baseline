"""
QUESTION:
Due to the rise of covid-19 cases in India, this year BCCI decided to organize knock-out matches in IPL rather than a league. 
Today is matchday 1 and it is between previous year winners Mumbai Indians and the city of Joy - Kolkata Knight Riders. Eoin Morgan the new captain of the team KKR, thinks that death overs are very important to win a match. He decided to end MI's innings with his most trusted bowler Pat Cummins to minimize the target. There must be at least 4 players inside the 30-yard circle in death overs. Positions of 3 players are already decided which are given as 2-D integer points A, B, and C,  the task is to find the missing point D such that ABCD should be a parallelogram. If there are multiple such points, find the lexicographically smallest coordinate.
 
Example 1:
Input:
A = (3, 2)
B = (3, 4)
c = (2, 2)
Output:
2.000000 0.000000
Explanation: There are two options for 
point D : (2, 4) and (2, 0) such that ABCD 
forms a parallelogram. Since (2, 0) is 
lexicographically smaller than (2, 4). Hence,
(2, 0) is the answer.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findPoint() which takes three lists of integers A[], B[] and C[] and return D[] list of two numbers with a precision of 6 decimal places where first element of D[ ] denote x coordinate and second element of D[ ] denote y coordinate.
Constraints:
1 ≤ x, y ≤ 1000, where x and y denote coordinates of points A, B, and C.
The order of points in the parallelogram doesnt matter.
The given points are not collinear.
"""

def find_missing_point(A, B, C):
    # Calculate possible coordinates for point D
    dx1 = B[0] - C[0]
    dy1 = B[1] - C[1]
    option1 = (A[0] + dx1, A[1] + dy1)
    option2 = (A[0] - dx1, A[1] - dy1)
    
    dx2 = A[0] - B[0]
    dy2 = A[1] - B[1]
    option3 = (C[0] + dx2, C[1] + dy2)
    option4 = (C[0] - dx2, C[1] - dy2)
    
    # Find the lexicographically smallest coordinate
    possible_points = [option1, option2, option3, option4]
    smallest_point = min(possible_points)
    
    # Return the smallest point with 6 decimal places
    return [round(smallest_point[0], 6), round(smallest_point[1], 6)]