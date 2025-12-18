"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Rahul and Rashi are off to the wedding of a close relative. This time they have to travel without their guardians. Rahul got very interested in the arrangement of seats inside the train coach.

The entire coach could be viewed as an arrangement of consecutive blocks of size 8.  

Berth Number   	Compartment

1 -  8               1  
9 - 16               2  
17 - 24               3  
... and so on

Each of these size-8 blocks are further arranged as:

1LB,  2MB,  3UB,  4LB,  5MB,  6UB,  7SL,  8SU  
9LB, 10MB, ...
...   
...

Here LB denotes lower berth, MB middle berth and UB upper berth.

The following berths are called Train-Partners:

3UB   |  6UB  
2MB   |  5MB  
1LB   |  4LB  
7SL   |  8SU  

and the pattern is repeated for every set of 8 berths.

Rahul and Rashi are playing this game of finding the train partner of each berth. Can you write a program to do the same?

------ Input ------ 

The first line of input contains a single integer T, denoting the number of test cases to follow.
Each of the next T lines contain a single integer N, the berth number whose neighbor is to be found out.

------ Output ------ 

The output should contain exactly T lines each containing the berth of the neighbor of the corresponding seat.

------ Constraints ------ 

------ Subtasks ------ 

Subtask #1 (50 points):
$1 ≤ T ≤ 8$
$1 ≤ N ≤ 8$

Subtask #2 (50 points):
$1 ≤ T ≤ 100$
$1 ≤ N ≤ 500$

----- Sample Input 1 ------ 
3
1
5
3
----- Sample Output 1 ------ 
4LB
2MB
6UB
"""

def find_train_partner(T, berth_numbers):
    results = []
    for n in berth_numbers:
        m = int(n // 8)
        l = n - m * 8
        if l == 7:
            results.append(f"{n + 1}SU")
        elif l == 0:
            results.append(f"{n - 1}SL")
        elif l == 6:
            results.append(f"{n - 3}UB")
        elif l == 3:
            results.append(f"{n + 3}UB")
        elif l == 5:
            results.append(f"{n - 3}MB")
        elif l == 2:
            results.append(f"{n + 3}MB")
        elif l == 4:
            results.append(f"{n - 3}LB")
        else:
            results.append(f"{n + 3}LB")
    return results