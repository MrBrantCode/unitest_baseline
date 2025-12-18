"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

A sequence of integers is beautiful if each element of this sequence is divisible by 4.

You are given a sequence a_{1}, a_{2}, ..., a_{n}. In one step, you may choose any two elements of this sequence, remove them from the sequence and append their sum to the sequence. Compute the minimum number of steps necessary to make the given sequence beautiful.

------ Input ------ 

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer n.
The second line contains n space-separated integers a_{1}, a_{2}, ..., a_{n}.

------ Output ------ 

For each test case, print a single line containing one number — the minimum number of steps necessary to make the given sequence beautiful. If it's impossible to make the sequence beautiful, print -1 instead.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ n ≤ 10^{5}$
$1 ≤ sum of n over all test cases ≤ 10^{6}$
$0 ≤ a_{i} ≤ 10^{9}$

----- Sample Input 1 ------ 
1
7
1 2 3 1 2 3 8
----- Sample Output 1 ------ 
3
"""

def make_sequence_beautiful(test_cases):
    results = []
    
    for t, num in test_cases:
        if sum(num) % 4 == 0:
            num = [j % 4 for j in num if j % 4 != 0]
            a1 = num.count(1)
            a2 = num.count(2)
            a3 = num.count(3)
            
            if a1 == a3:
                ans = a1 + a2 // 2
            elif a1 < a3:
                c3 = a3 - a1
                if c3 % 4 == 0:
                    a = c3 // 4 * 3
                elif c3 % 4 == 2:
                    a = c3 // 4 * 3 + 2
                ans = a1 + a + a2 // 2
            elif a3 < a1:
                c1 = a1 - a3
                if c1 % 4 == 0:
                    a = c1 // 4 * 3
                elif c1 % 4 == 2:
                    a = c1 // 4 * 3 + 2
                ans = a3 + a + a2 // 2
            results.append(ans)
        else:
            results.append(-1)
    
    return results