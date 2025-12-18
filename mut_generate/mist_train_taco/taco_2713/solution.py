"""
QUESTION:
A programming competition site AtCode provides algorithmic problems.
Each problem is allocated a score based on its difficulty.
Currently, for each integer i between 1 and D (inclusive), there are p_i problems with a score of 100i points.
These p_1 + … + p_D problems are all of the problems available on AtCode.
A user of AtCode has a value called total score.
The total score of a user is the sum of the following two elements:
 - Base score: the sum of the scores of all problems solved by the user.
 - Perfect bonuses: when a user solves all problems with a score of 100i points, he/she earns the perfect bonus of c_i points, aside from the base score (1 ≤ i ≤ D).
Takahashi, who is the new user of AtCode, has not solved any problem.
His objective is to have a total score of G or more points.
At least how many problems does he need to solve for this objective?

-----Constraints-----
 - 1 ≤ D ≤ 10
 - 1 ≤ p_i ≤ 100
 - 100 ≤ c_i ≤ 10^6
 - 100 ≤ G
 - All values in input are integers.
 - c_i and G are all multiples of 100.
 - It is possible to have a total score of G or more points.

-----Input-----
Input is given from Standard Input in the following format:
D G
p_1 c_1
:
p_D c_D

-----Output-----
Print the minimum number of problems that needs to be solved in order to have a total score of G or more points. Note that this objective is always achievable (see Constraints).

-----Sample Input-----
2 700
3 500
5 800

-----Sample Output-----
3

In this case, there are three problems each with 100 points and five problems each with 200 points. The perfect bonus for solving all the 100-point problems is 500 points, and the perfect bonus for solving all the 200-point problems is 800 points. Takahashi's objective is to have a total score of 700 points or more.
One way to achieve this objective is to solve four 200-point problems and earn a base score of 800 points. However, if we solve three 100-point problems, we can earn the perfect bonus of 500 points in addition to the base score of 300 points, for a total score of 800 points, and we can achieve the objective with fewer problems.
"""

def minimum_problems_to_solve(D, G, problems):
    ans = float('inf')
    
    for i in range(2 ** D):
        score = 0
        cnt = 0
        rest = []
        
        for j in range(D):
            if i >> j & 1:
                score += 100 * (j + 1) * problems[j][0] + problems[j][1]
                cnt += problems[j][0]
            else:
                rest.append(j)
        
        if score < G:
            if rest:
                r = rest[-1]
                for _ in range(problems[r][0] - 1):
                    score += 100 * (r + 1)
                    cnt += 1
                    if score >= G:
                        break
        
        if score >= G:
            ans = min(cnt, ans)
    
    return ans