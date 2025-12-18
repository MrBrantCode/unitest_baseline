"""
QUESTION:
You are a coach at your local university. There are $n$ students under your supervision, the programming skill of the $i$-th student is $a_i$.

You have to create a team for a new programming competition. As you know, the more students some team has the more probable its victory is! So you have to create a team with the maximum number of students. But you also know that a team should be balanced. It means that the programming skill of each pair of students in a created team should differ by no more than $5$.

Your task is to report the maximum possible number of students in a balanced team.


-----Input-----

The first line of the input contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of students.

The second line of the input contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^9$), where $a_i$ is a programming skill of the $i$-th student.


-----Output-----

Print one integer — the maximum possible number of students in a balanced team.


-----Examples-----
Input
6
1 10 17 12 15 2

Output
3

Input
10
1337 1337 1337 1337 1337 1337 1337 1337 1337 1337

Output
10

Input
6
1 1000 10000 10 100 1000000000

Output
1



-----Note-----

In the first example you can create a team with skills $[12, 17, 15]$.

In the second example you can take all students in a team because their programming skills are equal.

In the third example you can create a team consisting of a single student (and you cannot create a team consisting of at least two students).
"""

def max_balanced_team_size(n, skills):
    skills.sort()
    skills.append(1000000006)  # Append a large number to handle edge cases
    maxcnt = 1
    first = 0
    last = 1
    
    for i in range(1, n + 1):
        if skills[i] - skills[first] > 5:
            first += 1
        elif i - first + 1 > maxcnt:
            maxcnt = i - first + 1
    
    return maxcnt