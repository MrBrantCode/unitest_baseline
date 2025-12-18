"""
QUESTION:
A file contains data as follows : {Student name, marks in 3 subjects}.
There are N students in a class. Find the student who has maximum average score.
Note: The average score is always floored.
 
Example 1:
Input:
N = 2
S = {"Shrikanth 20 30 10", "Ram 100 50 10"}
Output:
Ram 53
Explantion:
Shrikanth has an average of 20, whereas
Ram has a average of 53. So, Ram has the
maximum average.
Example 2:
Input:
N = 3
S = {"Adam 50 10 40", "Rocky 100 90 10", "Suresh 10 90 100"}
Output:
Rocky Suresh 66
Explantion:
Rocky and Suresh both have an average of 66, which is the
highest in the class.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function studentRecord() which takes an Integer N and a vector of vector of strings where each string vector contains 4 space separated inputs, the first being the name of the student and the rest being the marks of the student. The function should return a string consisting of two or more words where the last word is the max average of the class and the preceding words are names of student/s who have the max average. The names of the students should appear in the same order as they are given in the Input.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{4}
1 <= marks <= 100
1 <= Length of the Name <= 10
"""

def find_student_with_max_average(N, S):
    max_avg = 0
    max_avg_students = []
    
    for student in S:
        name = student[0]
        marks = list(map(int, student[1:4]))
        avg = sum(marks) // 3
        
        if avg > max_avg:
            max_avg = avg
            max_avg_students = [name]
        elif avg == max_avg:
            max_avg_students.append(name)
    
    result = ' '.join(max_avg_students) + ' ' + str(max_avg)
    return result