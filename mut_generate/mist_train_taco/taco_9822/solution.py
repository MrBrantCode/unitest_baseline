"""
QUESTION:
Currently, people's entertainment is limited to programming contests. The activity of the entertainment club of a junior high school to which she belongs is to plan and run a programming contest. Her job is not to create problems. It's a behind-the-scenes job of soliciting issues from many, organizing referees, and promoting the contest. Unlike charismatic authors and prominent algorithms, people who do such work rarely get the light. She took pride in her work, which had no presence but was indispensable.

The entertainment department is always looking for problems, and these problems are classified into the following six types.

* Math
* Greedy
* Geometry
* DP
* Graph
* Other



Fortunately, there were so many problems that she decided to hold a lot of contests. The contest consists of three questions, but she decided to hold four types of contests to make the contest more educational.

1. Math Game Contest: A set of 3 questions including Math and DP questions
2. Algorithm Game Contest: A set of 3 questions, including Greedy questions and Graph questions.
3. Implementation Game Contest: A set of 3 questions including Geometry questions and Other questions
4. Well-balanced contest: 1 question from Math or DP, 1 question from Greedy or Graph, 1 question from Geometry or Other, a total of 3 question sets



Of course, questions in one contest cannot be asked in another. Her hope is to hold as many contests as possible. I know the stock numbers for the six questions, but how many times can I hold a contest? This is a difficult problem for her, but as a charismatic algorithm, you should be able to solve it.



Input

The input consists of multiple cases. Each case is given in the following format.


nMath nGreedy nGeometry nDP nGraph nOther


The value of each input represents the number of stocks of each type of problem.

The end of input


0 0 0 0 0 0

Given by a line consisting of.

Each value satisfies the following conditions.
nMath + nGreedy + nGeometry + nDP + nGraph + nOther ≤ 100,000,000


The number of test cases does not exceed 20,000.

Output

Output the maximum number of contests that can be held on one line.

Example

Input

1 1 1 1 1 1
1 1 1 0 0 0
1 0 0 0 1 1
3 0 0 3 0 0
3 1 0 1 3 1
1 2 0 2 0 1
0 0 1 1 0 3
1 0 0 1 1 0
0 0 0 0 0 0


Output

2
1
1
2
3
1
1
0
"""

def calculate_max_contests(nMath, nGreedy, nGeometry, nDP, nGraph, nOther):
    # Initialize arrays to keep track of problem counts and contest types
    n = [0] * 3
    k = [0] * 3
    f = [0] * 3
    
    # Combine Math and DP, Greedy and Graph, Geometry and Other
    for i in range(3):
        n[i] += [nMath, nGreedy, nGeometry][i] + [nDP, nGraph, nOther][i]
    
    ans = 0
    
    # Calculate the number of contests for each type
    for i in range(3):
        if n[i] >= 3:
            f[i] = 1
        ans += n[i] // 3
        n[i] %= 3
        k[n[i]] += 1
    
    # Adjust the number of contests based on remaining problems
    if k[0] > 0:
        if k[2] == 2:
            i = 0
            while n[i]:
                i += 1
            if f[i]:
                ans += 1
    elif k[1] > 0:
        ans += 1
    elif k[2] > 0:
        ans += 2
    
    return ans