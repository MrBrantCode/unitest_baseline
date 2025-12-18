"""
QUESTION:
Read problems statements in [Mandarin Chinese], [Russian], and [Bengali] as well.

A programming competition will be held in Chef's city which only accepts teams of size 2. At least one person in a team should know a programming language and at least one person should know about the English language. It is possible that one person in a team knows both programming and the English language. Then the qualification of the other teammate is not important i.e. he may or may not know programming and English. Now Chef has N students and wants to send *maximum* number of teams to the competition.

You are given an integer N and two binary strings S and T of length N. S_{i} =  '1' denotes that the i^{th} student knows a programming language, and S_{i} =  '0' denotes otherwise; similarly, T_{i} = '1' denotes that the i^{th} student knows English language, and T_{i} =  '0' denotes otherwise. Determine the maximum number of teams Chef can form.

------ Input Format ------ 

- The first line of input contains a single integer Q denoting the number of test cases. The description of Q test cases follows.
- Each test case contains 3 lines of input.
- The first line of each test case contains an integer N.
- The second line of each test case contains a string S.
- The last line of each test case contains a string T.

------ Output Format ------ 

For each test case, print a single line containing one integer - the maximum number of teams that Chef can form.

------ Constraints ------ 

$1 ≤ Q ≤ 1000$
$1 ≤ N ≤ 100$
$S$ and $T$ contains only characters '0' and '1'

----- Sample Input 1 ------ 
4
3
101
001
4
1010
0110
3
000
110
2
10
11

----- Sample Output 1 ------ 
1
2
0
1

----- explanation 1 ------ 
Test case $1$: The third student can team up with any other students as he knows both programming and English.

Test case $2$: The first two students make a team and the last two students make another team.

Test case $3$: No student knows how to program, hence there is no way to make a team.
"""

def max_teams_for_competition(N, S, T):
    ps = 0  # Students who know programming but not English
    es = 0  # Students who know English but not programming
    bs = 0  # Students who know both programming and English
    ns = 0  # Students who know neither programming nor English
    
    for i in range(N):
        if S[i] == '1' and T[i] == '0':
            ps += 1
        elif T[i] == '1' and S[i] == '0':
            es += 1
        elif T[i] == '1' and S[i] == '1':
            bs += 1
        elif T[i] == '0' and S[i] == '0':
            ns += 1
    
    ans = 0
    ans += min(bs, ns)
    bs = bs - ns if bs > ns else 0
    ans += min(es, ps)
    rem = abs(es - ps)
    ans += min(rem, bs)
    bs = bs - rem if bs > rem else 0
    ans += bs // 2
    
    return ans