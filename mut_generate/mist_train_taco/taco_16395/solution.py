"""
QUESTION:
Last year Bob earned by selling memory sticks. During each of n days of his work one of the two following events took place: 

  * A customer came to Bob and asked to sell him a 2x MB memory stick. If Bob had such a stick, he sold it and got 2x berllars. 
  * Bob won some programming competition and got a 2x MB memory stick as a prize. Bob could choose whether to present this memory stick to one of his friends, or keep it. 



Bob never kept more than one memory stick, as he feared to mix up their capacities, and deceive a customer unintentionally. It is also known that for each memory stick capacity there was at most one customer, who wanted to buy that memory stick. Now, knowing all the customers' demands and all the prizes won at programming competitions during the last n days, Bob wants to know, how much money he could have earned, if he had acted optimally.

Input

The first input line contains number n (1 ≤ n ≤ 5000) — amount of Bob's working days. The following n lines contain the description of the days. Line sell x stands for a day when a customer came to Bob to buy a 2x MB memory stick (0 ≤ x ≤ 2000). It's guaranteed that for each x there is not more than one line sell x. Line win x stands for a day when Bob won a 2x MB memory stick (0 ≤ x ≤ 2000).

Output

Output the maximum possible earnings for Bob in berllars, that he would have had if he had known all the events beforehand. Don't forget, please, that Bob can't keep more than one memory stick at a time.

Examples

Input

7
win 10
win 5
win 3
sell 5
sell 3
win 10
sell 10


Output

1056


Input

3
win 5
sell 6
sell 4


Output

0
"""

def calculate_max_earnings(n, events):
    L = [-1] * 2010
    DP = [0] * 5010
    
    for i in range(n):
        (type, cost) = events[i]
        cost = int(cost)
        if type == 'win':
            L[cost] = i
        elif L[cost] >= 0:
            DP[i + 1] = DP[L[cost]] + 2 ** cost
        DP[i + 1] = max(DP[i], DP[i + 1])
    
    return DP[n]