"""
QUESTION:
Recently Chef joined a new company. In this company, the employees have to work for X hours each day from Monday to Thursday. Also, in this company, Friday is called Chill Day — employees only have to work for Y hours (Y < X) on Friday. Saturdays and Sundays are holidays.

Determine the total number of working hours in one week.

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers X and Y — the number of working hours on each day from Monday to Thursday and the number of working hours on Friday respectively.

------ Output Format ------ 

For each test case, output the total number of working hours in one week.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$2 ≤ X ≤ 12$
$1 ≤Y < X$

----- Sample Input 1 ------ 
3
10 5
12 2
8 7

----- Sample Output 1 ------ 
45
50
39

----- explanation 1 ------ 
Test case $1$: The total number of working hours in a week are: $10 \texttt{(Monday)} + 10 \texttt{(Tuesday)} + 10 \texttt{(Wednesday)} + 10 \texttt{(Thursday)} + 5 \texttt{(Friday)} = 45$

Test Case 2: The total number of working hours in a week are: $12 \texttt{(Monday)} + 12 \texttt{(Tuesday)} + 12 \texttt{(Wednesday)} + 12 \texttt{(Thursday)} + 2 \texttt{(Friday)} = 50$

Test Case 3: The total number of working hours in a week are: $8 \texttt{(Monday)} + 8 \texttt{(Tuesday)} + 8 \texttt{(Wednesday)} + 8 \texttt{(Thursday)} + 7 \texttt{(Friday)} = 39$
"""

def calculate_weekly_working_hours(test_cases):
    results = []
    for x, y in test_cases:
        total_hours = x * 4 + y
        results.append(total_hours)
    return results