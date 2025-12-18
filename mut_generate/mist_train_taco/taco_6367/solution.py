"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

When the final results for the employement competition were announced, Nour Eddin Ramadan was thrilled to find his name among the accepted co-Chefs.

However, after a while Nour started wasting time at the kitchen. He would usually spend hours talking to girls, and he even invited a girl to the kitchen pretending that he is the most valuable employer at Chef's restaurant.

When Chef found out about it, he decided that it was time to teach Nour a lesson. Before going home that night, Chef called Nour to his office and asked him to solve the following problem, saying that he better come to work tomorrow with a solution for it, or otherwise, it would be better if he doesn't come at all:

Given T queries, where each query contains a single number Y, Nour has to find the number of pairs A and B, such that the following equation holds true:

A^{2} + B ≤ Y

Where A is any positive integer, and B holds (1 ≤ B ≤ 700).

Nour was really busy that night (Yeah he got that girl to go out with him after all!), and he asked for your help.
 
------ Input ------ 

The first line contains T denoting the number of test cases.

T lines follows, Each line contains a single integer Y denoting the right side of the formula.

------ Output ------ 

For each test print a single line, containing a single number, indicating the answer for the test.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ Y ≤ 10^{10}$
$Note that A must be any positive integer, and B must hold 1 ≤ B ≤ 700.$

----- Sample Input 1 ------ 
4

2

3

4

10000000000
----- Sample Output 1 ------ 
1

2

3

69999300
"""

import math

def count_valid_pairs(T, Y_list):
    results = []
    for n in Y_list:
        if n > 700:
            x = n - 700
            v = math.floor(math.sqrt(x))
            u = math.ceil(math.sqrt(n) - 1)
            ans = 700 * v
            y = (u - v) * n - u * (u + 1) * (2 * u + 1) // 6 + v * (v + 1) * (2 * v + 1) // 6
            ans += y
        else:
            u = math.ceil(math.sqrt(n) - 1)
            ans = u * n - u * (u + 1) * (2 * u + 1) // 6
        results.append(ans)
    return results