"""
QUESTION:
Alice and Bob were having an argument about which of them is taller than the other. Charlie got irritated by the argument, and decided to settle the matter once and for all.

Charlie measured the heights of Alice and Bob, and got to know that Alice's height is X centimeters and Bob's height is Y centimeters. Help Charlie decide who is taller.

It is guaranteed that X \neq Y.

------ Input Format ------ 

- The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
- The first and only line of each test case contains two integers X and Y, as described in the problem statement. 

------ Output Format ------ 

For each test case, output on a new line \texttt{A} if Alice is taller than Bob, else output \texttt{B}. 
The output is case insensitive, i.e, both \texttt{A} and \texttt{a} will be accepted as correct answers when Alice is taller.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$100 ≤ X, Y ≤ 200$
$X \neq Y$

----- Sample Input 1 ------ 
2
150 160
160 150
----- Sample Output 1 ------ 
B
A
----- explanation 1 ------ 
Test case $1$: In this case, $150 < 160$ so Bob is taller than Alice.

Test case $2$: In this case, $160 > 150$ so Alice is taller than Bob.
"""

def determine_taller_person(test_cases):
    results = []
    for x, y in test_cases:
        if x > y:
            results.append('A')
        else:
            results.append('B')
    return results