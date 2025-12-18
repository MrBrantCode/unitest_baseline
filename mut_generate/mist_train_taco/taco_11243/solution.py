"""
QUESTION:
The time is 2020. There is data that saves the qualifying results of PC Koshien 2020. This data stores the reference number and the number of correct answers assigned to each team. Here, the ranking is determined by the number of correct answers, and the ranking is given in descending order of the number of correct answers, such as 1st, 2nd, and so on.

Enter the qualifying result data and reference number from the keyboard, and create a program that outputs the ranking of the team with that number.

Note

In the data of the input example, if the teams are arranged in order of the number of correct answers:


3,30
1,20
2,20
6,20
4,10
5,10


It will be. Here, in order to determine the ranking based on the number of correct answers, the 30-question correct answer team is ranked 1st, the 20-question correct answer team is ranked 2nd, and the 10-question correct answer team is ranked 3rd. Please note that this is different from the usual ranking with the correct team in 5th place).



Input

The input data consists of two parts. The first half is the qualifying result data, and the second half is the inquiry of the team number for which you want to know the ranking. The format of the qualifying result data is as follows.


p1, s1
p2, s2
...
...
0,0


pi (1 ≤ pi ≤ 100) and si (0 ≤ si ≤ 30) are integers representing the reference number and the number of correct answers for the i-th team, respectively. It is assumed that the input of this data is completed when both the reference number and the number of correct answers are 0.

Then multiple inquiries in the second half are given. The inquiry format is as follows.


q1
q2
::


Each query is given the reference number qi (1 ≤ qi ≤ 30) on one line. Please process this until the end of the input. The number of inquiries does not exceed 100.

Output

For each inquiry, print the team ranking on one line.

Example

Input

1,20
2,20
3,30
4,10
5,10
6,20
0,0
1
2
4
5


Output

2
2
3
3
"""

def get_team_ranking(qualifying_results, queries):
    # Initialize data structures
    teams = [0] * 101  # To store the number of correct answers for each team
    points = [False] * 31  # To track which points have been achieved

    # Process qualifying results
    for ref_num, correct_answers in qualifying_results:
        if ref_num == 0 and correct_answers == 0:
            break
        teams[ref_num] = correct_answers
        points[correct_answers] = True

    # Calculate rankings for each query
    rankings = []
    for query in queries:
        p = teams[query]
        rank = 0
        for i in range(30, -1, -1):
            if points[i]:
                rank += 1
            if i == p:
                break
        rankings.append(rank)

    return rankings