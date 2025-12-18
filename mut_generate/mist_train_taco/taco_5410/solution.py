"""
QUESTION:
A: four tea

problem

Tea is indispensable for programming contests. Tea has the effect of relieving constant tension [citation needed]

There are N players participating in the contest, so I would like to prepare tea for this number of people. There are four types of tea packages, A, B, C, and D, all of which are the same variety but have different contents. For a package X, the price of one package is p_X yen, and it is known that if you buy one, you can make t_X cups of tea.

Find the minimum amount needed to make tea for N people. You may have a package that you don't buy at all, and you don't have to buy a package for just N people (if you can make more than N people).

Input format

The input is given in the following format.


N
p_A p_B p_C p_D
t_A t_B t_C t_D


* The first line gives the number of players participating in the contest.
* In the second line, the prices of tea in packages A, B, C and D are given separated by blanks.
* The third line gives the number of cups of tea that can be made from packages A, B, C, and D, separated by blanks.



Constraint

* 1 \ leq N \ leq 100
* 1 \ leq p_X \ leq 100
* 1 \ leq t_X \ leq 100
* All inputs are given as integers.



Output format

Output the minimum amount required to make tea for N people in one line.

Input example 1


Ten
1 2 3 4
1 2 4 8


Output example 1


6

* It's best to buy one package B and one D.



Input example 2


Five
2 9 9 8
1 4 5 100


Output example 2


8

* You will have 20 times more tea than you need, but buying one Package D is the cheapest way to get more than 5 cups of tea.



Input example 3


twenty four
2 3 4 7
7 9 11 20


Output example 3


8

* It's best to buy two packages A and one C. It may not be possible to make just enough tea for the number of people as in this case.





Example

Input

10
1 2 3 4
1 2 4 8


Output

6
"""

def calculate_minimum_tea_cost(N, prices, capacities):
    p_A, p_B, p_C, p_D = prices
    t_A, t_B, t_C, t_D = capacities
    
    r = range(N + 1)
    m = 1000000000.0
    
    for i in r:
        for j in r:
            for k in r:
                l = 0 - -(N - t_A * i - t_B * j - t_C * k) // t_D
                m = min(m, p_A * i + p_B * j + p_C * k + p_D * l * (l >= 0))
    
    return int(m)