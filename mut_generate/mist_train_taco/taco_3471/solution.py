"""
QUESTION:
Chef was driving on a highway at a speed of X km/hour.

To avoid accidents, there are fine imposed on overspeeding as follows:
No fine if the speed of the car ≤ 70 km/hour.
Rs 500 fine if the speed of the car is strictly greater than 70 and ≤ 100.
Rs 2000 fine if the speed of the car is strictly greater than 100.

Determine the fine Chef needs to pay.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single integer X denoting the speed of Chef's car.

------ Output Format ------ 

For each test case, output the fine paid by Chef.

------ Constraints ------ 

$1 ≤ T ≤ 200$
$1 ≤ X ≤ 200$

----- Sample Input 1 ------ 
7
40
110
70
100
69
101
85

----- Sample Output 1 ------ 
0
2000
0
500
0
2000
500

----- explanation 1 ------ 
Test case $1$: The speed is $≤ 70$. Thus, Chef does not need to pay any fine.

Test case $2$: The speed is greater than $100$. Thus, Chef needs to pay $2000$ as fine.

Test case $3$: The speed is $≤ 70$. Thus, Chef does not need to pay any fine.

Test case $4$: The speed is greater than $70$ and $≤ 100$. Thus, Chef needs to pay $500$ as fine amount.

Test case $5$: The speed is $≤ 70$. Thus, Chef does not need to pay any fine.

Test case $6$: The speed is greater than $100$. Thus, Chef needs to pay $2000$ as fine.

Test case $7$: The speed is greater than $70$ and $≤ 100$. Thus, Chef needs to pay $500$ as fine amount.
"""

def calculate_fine(speed: int) -> int:
    if speed > 100:
        return 2000
    elif speed > 70:
        return 500
    else:
        return 0