"""
QUESTION:
Roy has played a lot of Mario that he got bored of playing it again and again. So now he wants to design a stage of Mario game.

Right now he is simply designing a group of walls using bricks that little Mario has to cross over. Little Mario cannot jump more than 3 bricks' height, so Roy cannot create a wall of height more than 3.

Roy has N number of bricks. Roy wants to make a group of walls such that height of no single wall exceeds 3.

For example if N = 8, one of the group of walls can be as follows:

Now Roy wonders how many different groups of walls can he generate for a given number of bricks.
(See Sample Test Case Explanation for clarification)

Input:
First line contains integer T, number of Test Cases. 
Next T lines each will contain integer N, number of bricks Roy has.

Output:
Print an integer in new line for each test case, number of different groups of walls.

Since answer can be very large, print it modulo 1000000007

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 100000

Sample Test Case Explanation:  For N = 3SAMPLE INPUT
1
3

SAMPLE OUTPUT
4
"""

MOD = 1000000007

def count_wall_groups(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    
    t1, t2, t3 = 1, 2, 4
    for _ in range(N - 3):
        ans = (t1 + t2 + t3) % MOD
        t1, t2, t3 = t2, t3, ans
    
    return ans