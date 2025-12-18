"""
QUESTION:
D: Indecision-Indecision-

problem

Ebi-chan has been addicted to gal games lately, and her goal now is to capture two heroines at the same time.

Ebi-chan can use several events to increase her liking from the heroine, but only one heroine can be selected for each event. However, Ebi-chan does not forget to follow the heroine that she did not choose, so the liking from the other heroine can be increased to some extent. However, not all events can be done because events are expensive.

By the way, indecisive Ebi-chan is wondering which heroine to perform each event with (or neither). Ebi-chan thinks that it is meaningless if only one heroine has a high liking, but the other has a low liking, so the ideal choice is to maximize the liking from the heroine who does not have a high liking.

At this time, find the maximum value of the liking from the heroine who does not have the high liking. In other words, as a result of selecting the event and the target heroine, find the maximum value that can be considered as min \\ {A, B \\} when the favorability from the two heroines is A and B, respectively. Here, the total cost of the event you decide to do must not exceed your budget. Also, the initial value of favorability from each heroine is 0.

Input format


N C
a_1 b_1 c_1
...
a_N b_N c_N


The first line gives the number of candidate events N and the budget C, separated by blanks.

Line 1 + i (1 \ leq i \ leq N) contains the increment of favorability a_i of the heroine doing it, the increment of favorability b_i of the other heroine, and the cost c_i for the i-th event. Given with a space delimiter.

Constraint

* 1 \ leq N \ leq 100
* 1 \ leq C \ leq 100
* 1 \ leq b_i <a_i \ leq 100
* 1 \ leq c_i \ leq 100



Output format

Under the ideal selection in the question sentence, output the maximum value of the liking from the heroine who does not have the high liking in one line.

Input example 1


3 4
3 2 2
2 1 1
2 1 1


Output example 1


Five

It's best to have the first two events with one heroine and the last event with the other heroine.

Input example 2


3 3
3 2 2
2 1 1
2 1 1


Output example 2


Four





Example

Input

3 4
3 2 2
2 1 1
2 1 1


Output

5
"""

def maximize_min_liking(N, C, events):
    L = 250
    dp = [[-10 ** 18] * (L + 1) for i in range(C + 1)]
    
    for j in range(C + 1):
        dp[j][0] = 0
    
    for (a, b, c) in events:
        for j in range(C - c, -1, -1):
            for k in range(L + 1):
                if k + (b - a) <= 0:
                    dp[j + c][a - k - b] = max(dp[j + c][a - k - b], dp[j][k] + k + b)
                else:
                    dp[j + c][k + b - a] = max(dp[j + c][k + b - a], dp[j][k] + a)
                if k + (a - b) <= L:
                    dp[j + c][k + a - b] = max(dp[j + c][k + a - b], dp[j][k] + b)
    
    ans = 0
    for j in range(C + 1):
        ans = max(ans, max(dp[j]))
    
    return ans