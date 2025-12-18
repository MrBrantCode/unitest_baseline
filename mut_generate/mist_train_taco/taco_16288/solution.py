"""
QUESTION:
Read problems statements in mandarin chinese, russian and vietnamese as well. 

This year CodeChef is organizing the SnackUp cooking contest. The favorite to win is of course our beautiful Chef Ada.

There are n judges in the contest, and for simplicity let's enumerate judges from 1 to n. 

Ada has an uncountable repertoire of delicious recipes, but for the contest she choose only n of them. Let's also enumerate the recipes from 1 to n.

Ada is going to show off her cooking skills in many rounds, and we are going to help her organizing them! One round is structured as follows:
We will choose k distinct recipes and Ada will prepare two identical dishes for each of them.
We will choose k distinct judges for the round.
We will send k invitation letters (one for each of the chosen judges). Each letter must contain the number of the judge, and two distinct integers denoting the ids of the recipes that he is going to taste. 
Two different judges can taste the same recipe, but it must be from different dishes. 
Ada does not like to waste food, so the letters must be designed in such a way that every prepared dish is tasted.

You can arbitrarily decide the number of rounds and the number of invited judges in each round, but as a rule of the contest at the end of all rounds each judge must have tasted every recipe exactly twice.

------ Input ------ 

The first line of input contains one number T, the number of test cases.
Each test case consist of one line containing an integer n, the number of judges.

------ Output ------ 

For each testcase, in the first line, print r the number of rounds, then describe each round as follows.

In the first line of each round, print k, the number of invited judges.
In the next k lines, print the invitation letters as three space separated integers: j, x, y denoting the id of the judge, and the ids of the recipe that he is going to taste. Note that x should not be equal to y.

------ Constraints ------ 

1 ≤ T ≤ 100
2 ≤ n ≤ 100

----- Sample Input 1 ------ 
1
2
----- Sample Output 1 ------ 
2
2
1 1 2
2 1 2
2
1 1 2
2 1 2
"""

def generate_snackup_schedule(n):
    """
    Generates the schedule for the SnackUp cooking contest.

    Parameters:
    n (int): The number of judges and recipes.

    Returns:
    list: A list of strings representing the output for each test case.
    """
    arr = [(i, i + 1) for i in range(1, n)]
    arr.append((1, n))
    result = []
    result.append(f"{n}")
    for i in range(n):
        result.append(f"{n}")
        for j in range(n):
            result.append(f"{j + 1} {arr[(i + j) % n][0]} {arr[(i + j) % n][1]}")
    return result

def snackup_contest(T, test_cases):
    """
    Processes multiple test cases for the SnackUp cooking contest.

    Parameters:
    T (int): The number of test cases.
    test_cases (list): A list of integers, each representing the number of judges for each test case.

    Returns:
    list: A list of lists, where each inner list contains the output strings for a single test case.
    """
    results = []
    for n in test_cases:
        results.append(generate_snackup_schedule(n))
    return results