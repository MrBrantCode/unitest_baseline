"""
QUESTION:
Big P has become a Physical Education teacher at Hack International School.

Today, the students of class XII have been very undisciplined and he decides to punish them all.

He makes all of the N student (numbered 1 to N ) to stand in a line and asks them to sit down on their knees.

Students know that Big P is a very cruel and sadistic person and students start to sit down themselves when they see a friend sit down.

However, there are always some students who do not follow the trend. Now when Big P sees that happen , he slaps that student and makes him sit down. The same process as above is followed and is stopped when any - one student in the line refuses to sit down by himself.  

Given the students that Big P slaps to make them sit down , you need to tell the total no. of students who sat down in that line.

Note:  It is not necessary that if A is friend of B then B is also friend of A.

Input Format :
First Line Contains an integer T denoting no of test cases. 
Each test case begins with a line containing three integers N, F, S where N is the number of students in the line.         Next F lines have two integers A and B denoting the friendship between the students A and B.   Next S lines have one integer X denoting the student that was slapped by Big P .  

Output Format:
For each test case, output a line containing one integer, the total number of students that sit down in that line.

 T ≤ 10 , N ,F , S ≤ 10000 

SAMPLE INPUT
1
3 2 1
1 2
2 3
2

SAMPLE OUTPUT
2
"""

def calculate_students_sat_down(N, F, S, friendships, slapped_students):
    # Initialize data structures
    frndsip_map = {i: [] for i in range(1, N + 1)}
    studentlist = [False] * N
    visitlist = {i: False for i in range(1, N + 1)}
    
    # Populate friendship map
    for A, B in friendships:
        frndsip_map[A].append(B)
    
    # Mark slapped students as visited
    for student in slapped_students:
        visitlist[student] = True
    
    # Function to recursively mark friends as sitting down
    def color_it(i):
        if len(frndsip_map[i]) > 0:
            for j in frndsip_map[i]:
                if not visitlist[j]:
                    studentlist[j - 1] = True
                    visitlist[j] = True
                    color_it(j)
    
    # Process each slapped student
    for i in slapped_students:
        studentlist[i - 1] = True
        color_it(i)
    
    # Count the number of students who sat down
    return sum(studentlist)