"""
QUESTION:
There are $n$ consecutive seat places in a railway carriage. Each place is either empty or occupied by a passenger.

The university team for the Olympiad consists of $a$ student-programmers and $b$ student-athletes. Determine the largest number of students from all $a+b$ students, which you can put in the railway carriage so that:  no student-programmer is sitting next to the student-programmer;  and no student-athlete is sitting next to the student-athlete. 

In the other words, there should not be two consecutive (adjacent) places where two student-athletes or two student-programmers are sitting.

Consider that initially occupied seat places are occupied by jury members (who obviously are not students at all).


-----Input-----

The first line contain three integers $n$, $a$ and $b$ ($1 \le n \le 2\cdot10^{5}$, $0 \le a, b \le 2\cdot10^{5}$, $a + b > 0$) — total number of seat places in the railway carriage, the number of student-programmers and the number of student-athletes.

The second line contains a string with length $n$, consisting of characters "." and "*". The dot means that the corresponding place is empty. The asterisk means that the corresponding place is occupied by the jury member.


-----Output-----

Print the largest number of students, which you can put in the railway carriage so that no student-programmer is sitting next to a student-programmer and no student-athlete is sitting next to a student-athlete.


-----Examples-----
Input
5 1 1
*...*

Output
2

Input
6 2 3
*...*.

Output
4

Input
11 3 10
.*....**.*.

Output
7

Input
3 2 3
***

Output
0



-----Note-----

In the first example you can put all student, for example, in the following way: *.AB*

In the second example you can put four students, for example, in the following way: *BAB*B

In the third example you can put seven students, for example, in the following way: B*ABAB**A*B

The letter A means a student-programmer, and the letter B — student-athlete.
"""

import math

def max_students_in_carriage(n, a, b, seats):
    # Calculate the total number of students and determine the larger and smaller groups
    total_students = a + b
    max_students = max(a, b)
    min_students = total_students - max_students
    
    # Split the seats string into segments of consecutive empty seats
    empty_segments = seats.split('*')
    
    # Initialize the answer
    seated_students = 0
    
    # Process each segment of empty seats
    for segment in empty_segments:
        if '.' in segment:
            segment_length = len(segment)
            # Calculate the maximum number of students that can be seated in this segment
            max_in_segment = math.ceil(segment_length / 2)
            min_in_segment = math.floor(segment_length / 2)
            
            # Allocate seats to the larger group first
            seated_max = min(max_in_segment, max_students)
            seated_students += seated_max
            max_students -= seated_max
            
            # Allocate seats to the smaller group
            seated_min = min(min_in_segment, min_students)
            seated_students += seated_min
            min_students -= seated_min
            
            # Recalculate the larger and smaller groups
            total_students = max_students + min_students
            max_students = max(max_students, min_students)
            min_students = total_students - max_students
    
    return seated_students