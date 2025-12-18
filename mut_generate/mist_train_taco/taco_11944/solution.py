"""
QUESTION:
Little Elephant from the Zoo of Lviv likes cards. He has N cards, each of which has one of 1000 colors. The colors are numbered from 1 to 1000.
Little Elephant and Big Hippo are playing the following game. At first Little Elephant takes some subset of cards, and Big Hippo takes the rest of them. Here, Little Elephant can choose to take all of the cards, or none of the cards.
Then they play 1000 rounds: in round k (k = 1, 2, ..., 1000), they count the number of cards each has of the color k. Let Little Elephant has a cards of the color k, and Big Hippo has b cards of the color k. Then if a > b Little Elephant scores |a-b| points, otherwise Big Hippo scores |a-b| points in this round, where |x| denotes the absolute value of x.
You are given the number of cards N and the array C - list of colors of all N cards. Find the number of subsets (among all 2^{N} subsets) for which Little Elephant wins the game: that is, he gains more points than Big Hippo in total, if Little Elephant takes the subset at first. Since the answer can be large, print it modulo 1000000007 (10^{9}+7).

------ Input ------ 

First line of the input contains single integer T - the number of test cases. Then T test cases follow.
First line of each test case contains single integer N. Second line contains N integers separated by space - the array C.

------ Output ------ 

For each test case, print the answer in one line.

------ Constraints ------ 

1 ≤ T ≤ 100
1 ≤ N ≤ 1000
1 ≤ C_{i} ≤ 1000, where C_{i} denotes the i-th element of the array C

----- Sample Input 1 ------ 
2
3
1 2 3
4
1 1 3 2
----- Sample Output 1 ------ 
4
5
"""

def calculate_winning_subsets(n, colors):
    mod = 1000000007
    nn = 1005
    fac = [0] * nn
    fac[0] = 1
    for i in range(1, nn):
        fac[i] = fac[i - 1] * i
        fac[i] %= mod
    
    ans = 0
    if n % 2 == 1:
        end = n // 2 + 1
    else:
        end = n // 2
    
    for i in range(end):
        num = fac[n]
        den = fac[n - i] * fac[i]
        den %= mod
        inv = pow(den, mod - 2, mod)
        ans += num * inv % mod
        ans %= mod
    
    return ans