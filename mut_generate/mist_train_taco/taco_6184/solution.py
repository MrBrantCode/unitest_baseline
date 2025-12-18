"""
QUESTION:
JAG mock qualifying practice session

The ACM-ICPC OB / OG Association (Japanese Alumni Group; JAG) has N questions in stock of questions to be asked in the mock contest, and each question is numbered with an integer from 1 to N. Difficulty evaluation and recommendation voting are conducted for each problem. Problem i has a difficulty level of di and a recommendation level of vi. The maximum difficulty level is M.

In the next contest, we plan to ask a total of M questions, one for each of the difficulty levels 1 to M. In order to improve the quality of the contest, I would like to select the questions so that the total recommendation level is maximized. However, since JAG's questioning ability is tremendous, it can be assumed that there is at least one question for each difficulty level.

Your job is to create a program that finds the maximum sum of the sums of recommendations when the questions are selected to meet the conditions.

Input

The input consists of multiple datasets. Each dataset is represented in the following format.

> N M
> d1 v1
> ...
> dN vN
>

The first line of the dataset is given an integer N, which represents the number of problem stocks, and a maximum difficulty value, M, separated by blanks. These numbers satisfy 1 ≤ M ≤ N ≤ 100. On the i-th line of the following N lines, the integers di and vi representing the difficulty level and recommendation level of problem i are given, separated by blanks. These numbers satisfy 1 ≤ di ≤ M and 0 ≤ vi ≤ 100. Also, for each 1 ≤ j ≤ M, it is guaranteed that there is at least one i such that di = j.

> The end of the input is represented by two zeros separated by a blank. Also, the number of datasets does not exceed 50.

> ### Output

For each data set, output the maximum value of the sum of the recommendation levels of the questions to be asked when one question is asked from each difficulty level on one line.

> ### Sample Input


5 3
1 1
twenty three
3 2
3 5
twenty one
4 2
1 7
twenty one
13
1 5
6 1
13
1 2
1 8
1 2
1 7
1 6
20 9
4 10
twenty four
5 3
6 6
6 3
7 4
8 10
4 6
7 5
1 8
5 7
1 5
6 6
9 9
5 8
6 7
14
6 4
7 10
3 5
19 6
4 1
6 5
5 10
1 10
3 10
4 6
twenty three
5 4
2 10
1 8
3 4
3 1
5 4
1 10
13
5 6
5 2
1 10
twenty three
0 0



There are 5 sample datasets, in order
Lines 1 to 6 are the first (N = 5, M = 3) test cases,
Lines 7 to 11 are the second (N = 4, M = 2) test case,
Lines 12-18 are the third (N = 6, M = 1) test case,
The fourth (N = 20, M = 9) test case from line 19 to line 39,
Lines 40 to 59 represent the fifth test case (N = 19, M = 6).

Output for Sample Input


9
8
8
71
51





Example

Input

5 3
1 1
2 3
3 2
3 5
2 1
4 2
1 7
2 1
1 3
1 5
6 1
1 3
1 2
1 8
1 2
1 7
1 6
20 9
4 10
2 4
5 3
6 6
6 3
7 4
8 10
4 6
7 5
1 8
5 7
1 5
6 6
9 9
5 8
6 7
1 4
6 4
7 10
3 5
19 6
4 1
6 5
5 10
1 10
3 10
4 6
2 3
5 4
2 10
1 8
3 4
3 1
5 4
1 10
1 3
5 6
5 2
1 10
2 3
0 0


Output

9
8
8
71
51
"""

def maximize_recommendation_sum(N, M, problems):
    # Initialize a list to store the maximum recommendation for each difficulty level
    max_recommendations = [0] * M
    
    # Iterate through each problem to find the maximum recommendation for each difficulty level
    for d, v in problems:
        if max_recommendations[d - 1] < v:
            max_recommendations[d - 1] = v
    
    # Calculate the total maximum recommendation sum
    max_recommendation_sum = sum(max_recommendations)
    
    return max_recommendation_sum