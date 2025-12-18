"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

A *time* is a string in the format "HH:MM AM" or "HH:MM PM" (without quotes), where HH and MM are always two-digit numbers. A day starts at 12:00 AM and ends at 11:59 PM. You may refer [here] for understanding the 12-hour clock format.

Chef has scheduled a meeting with his friends at a time $P$. He has $N$ friends (numbered $1$ through $N$); for each valid $i$, the $i$-th friend is available from a time $L_{i}$ to a time $R_{i}$ (both inclusive). For each friend, can you help Chef find out if this friend will be able to attend the meeting? More formally, check if $L_{i} ≤ P ≤ R_{i}$ for each valid $i$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single time $P$.
The second line contains a single integer $N$.
$N$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated times $L_{i}$ and $R_{i}$.

------  Output ------
For each test case, print a single line containing one string with length $N$. For each valid $i$, the $i$-th character of this string should be '1' if $i$-th friend will be able to attend the meeting or '0' otherwise. 

------  Constraints  ------
$1 ≤ T ≤ 500$
$1 ≤ N ≤ 500$
each time is valid in the 12-hour clock format
for each valid $i$, the time $R_{i}$ is greater or equal to $L_{i}$

------  Subtasks ------
Subtask #1 (100 points): original constraints

----- Sample Input 1 ------ 
2

12:01 AM

4

12:00 AM 11:42 PM

12:01 AM 11:59 AM

12:30 AM 12:00 PM

11:59 AM 11:59 PM

04:12 PM

5

12:00 AM 11:59 PM

01:00 PM 04:12 PM

04:12 PM 04:12 PM

04:12 AM 04:12 AM

12:00 PM 11:59 PM
----- Sample Output 1 ------ 
1100

11101
----- explanation 1 ------ 
Example case 1: 
- Friend $1$: 12:01 AM lies between 12:00 AM and 11:42 PM (that is, between 00:00 and 23:42 in the 24-hour clock format), so this friend will be able to attend the meeting.
- Friend $2$: 12:01 AM lies between 12:01 AM and 11:59 AM (between 00:01 and 11:59 in the 24-hour clock format).
- Friend $3$: 12:01 AM does not lie between 12:30 AM and 12:30 PM (between 00:30 and 12:30 in the 24-hour clock format), so this friend will not be able to attend the meeting.
- Friend $4$: 12:01 AM does not lie between 11:59 AM and 11:59 PM (between 11:59 and 23:59 in the 24-hour clock format).

Example case 2: For friend $3$, 04:12 PM lies between 04:12 PM and 04:12 PM (inclusive) and hence this friend will be able to attend the meeting.
"""

def can_attend_meeting(P, N, availability):
    def min_conversion(p, h, m):
        if p == 'PM':
            if h != 12:
                h += 12
        elif h == 12:
            h -= 12
        return h * 60 + m
    
    x = P[-2:]
    t0 = P[:-3]
    (h0, m0) = map(int, t0.split(':'))
    final_t = min_conversion(x, h0, m0)
    
    result = []
    for i in range(N):
        (L, R) = availability[i]
        (d, e) = (L[-2:], R[-2:])
        (t1, t2) = (L[:-3], R[:-3])
        (h1, m1) = map(int, t1.split(':'))
        (h2, m2) = map(int, t2.split(':'))
        final_mins1 = min_conversion(d, h1, m1)
        final_mins2 = min_conversion(e, h2, m2)
        
        if final_mins1 <= final_t <= final_mins2:
            result.append('1')
        else:
            result.append('0')
    
    return ''.join(result)