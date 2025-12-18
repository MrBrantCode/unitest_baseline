"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

There are n villages in a line in an area. There are two kinds of tribes A and B that reside there. A village can be either empty or occupied by one of the tribes. An empty village is said to be controlled by a tribe of village A if it is surrounded by villages of tribes A from the left and from the right. Same goes for the tribe B.

Find out the number of villages that are either occupied by or controlled by tribes A and B, respectively.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases.
The first line of the input contains a string s denoting the configuration of the villages, each character of which can be 'A', 'B' or '.'.

------ Output ------ 

For each test case, output two space-separated integers denoting the number of villages either occupied by or controlled by tribe A and B, respectively.

------ Constraints ------ 

$1 ≤ T ≤ 20$
$1 ≤ |s| ≤ 10^{5}$

------ Subtasks ------ 

$Subtask #1 (40 points): 1 ≤ |s| ≤ 10^{3}$
$Subtask #2 (60 points): Original constraints$

----- Sample Input 1 ------ 
4
A..A..B...B
..A..
A....A
..B..B..B..
----- Sample Output 1 ------ 
4 5
1 0
6 0
0 7
"""

def count_controlled_villages(s: str) -> tuple[int, int]:
    count_A = 0
    count_B = 0
    consecutive_empty = 0
    last_tribe = ''
    
    for village in s:
        if village == '.':
            consecutive_empty += 1
        else:
            if village != last_tribe:
                consecutive_empty = 1
            if village == 'A':
                count_A += consecutive_empty
            else:
                count_B += consecutive_empty
            last_tribe = village
            consecutive_empty = 1
    
    return count_A, count_B