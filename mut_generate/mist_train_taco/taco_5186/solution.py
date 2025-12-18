"""
QUESTION:
Chef's college is conducting online exams. Chef has a test tomorrow and he being irresponsible failed to prepare for it on time (just as always). However, fortunately, he now realises the gravity of the situation and decides to prepare as much as possible in the time remaining and try to score maximum marks possible using his analytical skills. 

There are $N$ chapters and only $K$ minutes are left before the exam. Chapter $i$ will be worth $M_{i}$ marks in the exam, and shall take $T_{i}$ minutes to study. Chef can study the chapters in any order but needs to study them completely and at most once. He knows that he will forget the first chapter that he will prepare (due to lack of sleep) and won’t be able to score any marks in it. Find the maximum marks that Chef can score in the exam. 

Note that he cannot re-study the chapter that he has forgotten.

------ Input: ------

First line will contain $T$, number of testcases. Then the testcases follow. 
Each testcase contain $N + 1$ lines of input.
First line will contain $2$ space separated integers $N$ and $K$, total number of chapters and total time left before the exam respectively. 
Each of the next $N$ lines contain $2$ space separated integers $M_{i}$ and $T_{i}$, weightage and time for the $i^{th}$ chapter respectively.

------ Output: ------
For each testcase, output in a single line answer to the problem.

------ Constraints  ------
$1 ≤ T ≤ 10$
$1 ≤ N ≤ 10^{3}$
$1 ≤ K ≤ 10^{4}$
$1 ≤ M_{i} ≤ 10^{9}$
$1 ≤ T_{i} ≤ K$
Sum of $N * K$ over all tests is atmost $10^{7}$

----- Sample Input 1 ------ 
3

2 2

1 1

2 1

3 3

1 1

2 2

3 3

5 6

5 1

4 2

3 3

2 4

1 5
----- Sample Output 1 ------ 
2

2

9
----- explanation 1 ------ 
TestCase 1: Optimal solution is to study first chapter first followed by second chapter. So total marks ensured $= 1 + 2 - 1 = 2$

TestCase 2: Optimal solution is to study first chapter first followed by second chapter. So total marks ensured $= 1 + 2 - 1 = 2$

TestCase 3: Optimal solution is to study third chapter first followed by second and first chapter. So total marks ensured $= 3 + 4 + 5 - 3 = 9$
"""

def max_marks_with_forgetfulness(chapters, total_time):
    """
    Calculate the maximum marks Chef can score in the exam given the constraints.

    Parameters:
    - chapters (list of tuples): Each tuple contains (marks, time) for a chapter.
    - total_time (int): Total time left before the exam.

    Returns:
    - int: The maximum marks Chef can score.
    """
    n = len(chapters)
    dp = [[0, -float('inf')] for i in range(total_time + 1)]
    
    for i in range(n):
        (m, t) = chapters[i]
        for j in range(total_time, t - 1, -1):
            dp[j][0] = max(dp[j - t][0] + m, dp[j][0])
            dp[j][1] = max(dp[j][1], dp[j - t][0], dp[j - t][1] + m)
    
    return dp[total_time][1]