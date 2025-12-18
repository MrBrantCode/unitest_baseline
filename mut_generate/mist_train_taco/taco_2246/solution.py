"""
QUESTION:
Chef wants to become fit for which he decided to walk to the office and return home by walking. It is known that Chef's office is X km away from his home. 

If his office is open on 5 days in a week, find the number of kilometers Chef travels through office trips in a week.

------ Input Format ------ 

- First line will contain T, number of test cases. Then the test cases follow.
- Each test case contains of a single line consisting of single integer X.

------ Output Format ------ 

For each test case, output the number of kilometers Chef travels through office trips in a week.

------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ X ≤ 10$

----- Sample Input 1 ------ 
4
1
3
7
10

----- Sample Output 1 ------ 
10
30
70
100

----- explanation 1 ------ 
Test case $1$: The office is $1$ km away. Thus, to go to the office and come back home, Chef has to walk $2$ kms in a day. In a week with $5$ working days, Chef has to travel $2\cdot 5 = 10$ kms in total.

Test case $2$: The office is $3$ kms away. Thus, to go to the office and come back home, Chef has to walk $6$ kms in a day. In a week with $5$ working days, Chef has to travel $6\cdot 5 = 30$ kms in total.

Test case $3$: The office is $7$ kms away. Thus, to go to the office and come back home, Chef has to walk $14$ kms in a day. In a week with $5$ working days, Chef has to travel $14\cdot 5 = 70$ kms in total.

Test case $4$: The office is $10$ kms away. Thus, to go to the office and come back home, Chef has to walk $20$ kms in a day. In a week with $5$ working days, Chef has to travel $20\cdot 5 = 100$ kms in total.
"""

def calculate_weekly_travel_distance(test_cases):
    results = []
    for distance in test_cases:
        daily_distance = distance * 2  # Round trip distance
        weekly_distance = daily_distance * 5  # 5 working days in a week
        results.append(weekly_distance)
    return results