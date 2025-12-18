"""
QUESTION:
Berland State University invites people from all over the world as guest students. You can come to the capital of Berland and study with the best teachers in the country.

Berland State University works every day of the week, but classes for guest students are held on the following schedule. You know the sequence of seven integers $a_1, a_2, \dots, a_7$ ($a_i = 0$ or $a_i = 1$):  $a_1=1$ if and only if there are classes for guest students on Sundays;  $a_2=1$ if and only if there are classes for guest students on Mondays;  ...   $a_7=1$ if and only if there are classes for guest students on Saturdays. 

The classes for guest students are held in at least one day of a week.

You want to visit the capital of Berland and spend the minimum number of days in it to study $k$ days as a guest student in Berland State University. Write a program to find the length of the shortest continuous period of days to stay in the capital to study exactly $k$ days as a guest student.


-----Input-----

The first line of the input contains integer $t$ ($1 \le t \le 10\,000$) — the number of test cases to process. For each test case independently solve the problem and print the answer. 

Each test case consists of two lines. The first of them contains integer $k$ ($1 \le k \le 10^8$) — the required number of days to study as a guest student. The second line contains exactly seven integers $a_1, a_2, \dots, a_7$ ($a_i = 0$ or $a_i = 1$) where $a_i=1$ if and only if classes for guest students are held on the $i$-th day of a week.


-----Output-----

Print $t$ lines, the $i$-th line should contain the answer for the $i$-th test case — the length of the shortest continuous period of days you need to stay to study exactly $k$ days as a guest student.


-----Example-----
Input
3
2
0 1 0 0 0 0 0
100000000
1 0 0 0 1 0 1
1
1 0 0 0 0 0 0

Output
8
233333332
1



-----Note-----

In the first test case you must arrive to the capital of Berland on Monday, have classes on this day, spend a week until next Monday and have classes on the next Monday. In total you need to spend $8$ days in the capital of Berland.
"""

def find_minimum_stay_period(k, a):
    w = sum(a)
    ans = float('inf')
    
    # Case 1: k is less than or equal to the number of class days in a week
    if k <= w:
        for start in range(7):
            for end in range(start, 8):
                if sum(a[start:end]) >= k:
                    ans = min(ans, end - start)
    
    # Case 2: k is greater than the number of class days in a week
    for start in range(7):
        for end in range(7):
            x = sum(a[start:])
            y = sum(a[:end + 1])
            z = k - x - y
            if z >= 0 and z % w == 0:
                ans = min(ans, z // w * 7 + end + 1 + 7 - start)
    
    return ans