"""
QUESTION:
Finally, a basketball court has been opened in SIS, so Demid has decided to hold a basketball exercise session. $2 \cdot n$ students have come to Demid's exercise session, and he lined up them into two rows of the same size (there are exactly $n$ people in each row). Students are numbered from $1$ to $n$ in each row in order from left to right.

 [Image] 

Now Demid wants to choose a team to play basketball. He will choose players from left to right, and the index of each chosen player (excluding the first one taken) will be strictly greater than the index of the previously chosen player. To avoid giving preference to one of the rows, Demid chooses students in such a way that no consecutive chosen students belong to the same row. The first student can be chosen among all $2n$ students (there are no additional constraints), and a team can consist of any number of students. 

Demid thinks, that in order to compose a perfect team, he should choose students in such a way, that the total height of all chosen students is maximum possible. Help Demid to find the maximum possible total height of players in a team he can choose.


-----Input-----

The first line of the input contains a single integer $n$ ($1 \le n \le 10^5$) — the number of students in each row.

The second line of the input contains $n$ integers $h_{1, 1}, h_{1, 2}, \ldots, h_{1, n}$ ($1 \le h_{1, i} \le 10^9$), where $h_{1, i}$ is the height of the $i$-th student in the first row.

The third line of the input contains $n$ integers $h_{2, 1}, h_{2, 2}, \ldots, h_{2, n}$ ($1 \le h_{2, i} \le 10^9$), where $h_{2, i}$ is the height of the $i$-th student in the second row.


-----Output-----

Print a single integer — the maximum possible total height of players in a team Demid can choose.


-----Examples-----
Input
5
9 3 5 7 3
5 8 1 4 5

Output
29

Input
3
1 2 9
10 1 1

Output
19

Input
1
7
4

Output
7



-----Note-----

In the first example Demid can choose the following team as follows:  [Image] 

In the second example Demid can choose the following team as follows:  [Image]
"""

def max_team_height(n, row1, row2):
    if n == 0:
        return 0
    
    # Initialize the variables to store the maximum heights
    a0, b0 = 0, 0
    a1, b1 = row1[-1], row2[-1]
    
    # Iterate from the second last student to the first student
    for k in range(2, n + 1):
        a = row1[-k] + max(b0, b1)
        b = row2[-k] + max(a0, a1)
        
        # Update the variables for the next iteration
        a0, a1 = a1, a
        b0, b1 = b1, b
    
    # The result is the maximum of the last computed values
    return max(a1, b1)