"""
QUESTION:
problem

$ M $ students will be tested in a classroom with $ N $ seats in a straight line. Seats are numbered $ 1 \ dots N $ from the front, and $ 1 $ per seat can seat $ 1 $ students.

Now each student is sitting in the $ A_1, \ dots, A_M $ seats.

To start the test, the following conditions must be met:

* $ 1 \ dots M $ students are sitting in every seat.



Therefore, we decided to repeat the following operations until the conditions were met.

* Move the student sitting at the back and sit at the front of the vacant seats.



Find the number of operations required to meet the conditions.



output

Output the number of operations required to meet the conditions. Also, output a line break at the end.

Example

Input

6 4
1 4 5 6


Output

2
"""

def calculate_operations_to_meet_conditions(n, m, a):
    num = m
    for i in range(m):
        if a[i] <= m:
            num -= 1
    return num