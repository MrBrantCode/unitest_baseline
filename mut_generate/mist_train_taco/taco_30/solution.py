"""
QUESTION:
Nikit has to give a short contest of duration "n" minutes. The contest is divided into 2 sections-Easy and Hard. x and y marks will be awarded per problem for Easy and Hard respectively. Assume that he will take p minutes to solve an Easy problem and q minutes to solve a Hard problem successfully.
There are a and b number of Easy and  Hard problems respectively. Calculate how many problems of a particular section should he perform to get the maximum score in time.
Note: Assume he will always try to solve the easiest problem.
 
Example 1:
Input: n = 180, x = 2, y = 5, a = 4
b = 6,p = 20, q = 40
Output: 1 4
Explanation: Maximum marks get scored 
when he solves 1 easy and 4 hard problems.
Example 2:
Input: n = 50, x = 5, y = 10, a = 5 
b = 3, p = 10, q = 20
Output: 5 0
Explanation : Maximum marks gets scored 
when he solves 5 easy problems or 1 easy 
and 2 hard problems or 3 easy and 1 hard 
problem. But he always try to solve the 
easiest problem therefore solves 5 easy 
problems.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function maximumScore() which takes n, x, y, a, b, p, and q as input parameter and returns a list which contains the total number of easy problems and hard problems required to solve to get the maximum score.
 
Expected Time Complexity: O(a * b)
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 1000
1 <= x < y <= 100
1 <= a, b <= 100
1 <= p < q <= 100
"""

def maximum_score(n, x, y, a, b, p, q):
    max_score = 0
    best_combination = [0, 0]
    
    for i in range(a + 1):
        for j in range(b + 1):
            if i * p + j * q <= n:
                current_score = i * x + j * y
                if current_score > max_score:
                    max_score = current_score
                    best_combination = [i, j]
                elif current_score == max_score and i > best_combination[0]:
                    best_combination = [i, j]
    
    return best_combination