"""
QUESTION:
problem

N students from JOI High School are lined up in a row from east to west. The i-th student from the western end of the column is student i. Each student has a bib with one integer. Initially, the integer Ai is written on the number of student i.

There are M batons, and the batons are numbered from 1 to M. For k = 1, 2, ..., M, perform the following operations. The operation related to baton k (2 ≤ k ≤ M) is performed after the operation related to baton k -1 is completed.

1. The teacher gives the baton k to student 1.
2. Students who receive the baton pass the baton according to the following rules.
* Rule: Suppose student i receives the baton k.
* 1 ≤ i ≤ N-1: When the remainder of the integer of the number of student i divided by k is greater than the remainder of the integer of the number of student i + 1 divided by k, student i and student i + 1 exchanges the number, and student i passes the baton to student i + 1. Otherwise, student i passes the baton to student i + 1 without changing the bib.
* When i = N: Student N passes the baton to the teacher.
3. When the teacher receives the baton k from student N, the operation related to the baton k is finished.



Given the integer and the number of batons M that were originally written in the student number, write a program to find the integer of each student's number after the teacher receives the baton M from student N.

input

The input consists of 1 + N lines.

The integers N and M (1 ≤ N ≤ 100, 1 ≤ M ≤ 100) are written on the first line, separated by blanks, and represent the number of students and the number of batons, respectively.

The integer Ai (1 ≤ Ai ≤ 1000) is written on the i-th line (1 ≤ i ≤ N) of the following N lines, and represents the integer Ai first written on the number of student i.

output

The output consists of N lines. On line i (1 ≤ i ≤ N), output the integer of the number of student i after the teacher receives the baton M from student N.

Input / output example

Input example 1


6 4
3
2
8
3
1
Five


Output example 1


2
3
1
8
Five
3


Input example 2


10 6
1
2
3
Four
Five
6
7
8
9
Ten


Output example 2


6
1
2
3
Ten
Four
8
7
9
Five


Input / output example 1 has 6 students. Initially, the student numbers are 3, 2, 8, 3, 1, and 5, in that order. There are four batons.

* At the end of the operation related to baton 1, the student numbers are 3, 2, 8, 3, 1, and 5, respectively.
* At the end of the operation related to baton 2, the student numbers are 2, 8, 3, 3, 1, and 5, respectively.
* At the end of the operation related to baton 3, the student numbers are 2, 3, 3, 1, 8, and 5, respectively.
* At the end of the operation related to baton 4, the student numbers are 2, 3, 1, 8, 5, and 3 in order.



Creative Commons License

Information Olympics Japan Committee work "15th Japan Information Olympics JOI 2015/2016 Qualifying Competition Tasks"





Example

Input

6 4
3
2
8
3
1
5


Output

2
3
1
8
5
3
"""

def process_student_numbers(n, m, a):
    for i in range(1, m + 1):
        for j in range(n - 1):
            if a[j] % i > a[j + 1] % i:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a