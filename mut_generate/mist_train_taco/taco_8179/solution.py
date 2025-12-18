"""
QUESTION:
A: Taking a Seat-Taking a Seat-

story

Mr. A entered the classroom at the examination site to take an examination. However, Mr. A is a very nervous type. Therefore, depending on the situation, there may be seats that Mr. A does not want to sit in. Therefore, Mr. A decided to find out how many seats he could sit on based on certain conditions.

problem

Mr. A is a nervous type of person. First of all, Mr. A cannot sit in the first row from the front. Because when I sit near the proctor, I get nervous and can't solve the problem. Also, if there is a person on the right or left, Mr. A cannot sit down. This is because the sound of the pencil next to me makes it impossible to concentrate during the test. In addition, you can't sit near a noisy guy (near 8 diagonally up, down, left, and right). This is because my voice echoes in my head during the break and I can't rest. Also, it's natural, but I can't sit in the seat where the students are already sitting.

Is there a place where Mr. A can sit under these conditions? Assuming that M x N seats are lined up in the classroom, let's find the number.

Input format

The first row gives M (number of rows: number of vertical seats) and N (number of columns: number of horizontal seats). From the second line, M lines and a character string of length N are given line by line. The j character of the i-th character string represents the state of the seat in the i-th row and the j-th column. Each letter is either'-',' x'or'o', vacant seats'-', noisy students sitting during breaks'x', other students sitting' Let it be o'.

Constraint

* 0 <M ≤ 100
* 0 <N ≤ 100



Output format

Output the number of seats that Mr. A can sit in one line depending on the conditions. Don't forget the line break at the end.

Input example 1


5 5
--o--
--xo-
--x--
o --- x
--xoo


Output example 1


3

Input example 2


2 6
--oooo
x--o--


Output example 2


1

Input example 3


3 5
-----
-----
-----


Output example 3


Ten

Input example 4


4 6
o-oxoo
oo-ooo
oooxo-
o-ooox


Output example 4


0





Example

Input

5 5
--o--
--xo-
--x--
o---x
--xoo


Output

3
"""

def count_available_seats(m, n, seat_layout):
    # Add dummy rows and columns to handle boundary conditions
    dummy = ['0' for _ in range(n + 2)]
    for row in seat_layout:
        row.insert(0, '0')
        row.append('0')
    seat_layout.insert(0, dummy)
    seat_layout.append(dummy)
    
    # Mark seats that Mr. A cannot sit in
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seat_layout[i][j] == 'o':
                if seat_layout[i][j - 1] == '-':
                    seat_layout[i][j - 1] = '0'
                if seat_layout[i][j + 1] == '-':
                    seat_layout[i][j + 1] = '0'
            elif seat_layout[i][j] == 'x':
                for k in range(3):
                    for l in range(3):
                        if seat_layout[i - 1 + k][j - 1 + l] == '-':
                            seat_layout[i - 1 + k][j - 1 + l] = '0'
    
    # Mr. A cannot sit in the first row
    for i in range(n + 1):
        if seat_layout[1][i] == '-':
            seat_layout[1][i] = '0'
    
    # Count the remaining available seats
    count = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seat_layout[i][j] == '-':
                count += 1
    
    return count