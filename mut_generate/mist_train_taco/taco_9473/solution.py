"""
QUESTION:
Read problems statements in Mandarin Chinese and Russian as well. 

Mike takes part in programming contests. His favourite topic is dynamic programming(DP). As he said, that he likes problems on DP, because "you spend a lot of time on thinking and a little time on coding".
In this problem you are to solve a version of the knapsack problem(link), one of the most famous examples of DP problem.
You are given N items, each has two parameters: a weight and a cost. Let's define M as the sum of the weights of all the items.
Your task is to determine the most expensive cost of a knapsack, which capacity equals to 1, 2, ..., M. A cost of a knapsack equals to the sum of the costs of all the elements of the knapsack. Also, when you have a knapsack with a capacity is equal to C, then you can fill it with items, whose sum of weights is not greater than C.

------ Input ------ 

The first line of the input contains one integer N, denoting the number of the items.
The next N lines contain two integers W and C each, denoting the weight and the cost of the corresponding item.

------ Output ------ 

For each capacity C (1 ≤ C ≤ M) of the knapsack, output a single integer - the most expensive cost for that capacity.

------ Constraints ------ 

3 ≤ N ≤ 100000;
1 ≤ W ≤ 2, for each item;
1 ≤ C ≤ 10^{9}, for each item.

------ Example ------ 

Input:
5
1 1
2 2
2 3
2 4
2 5

Output:
1 5 6 9 10 12 13 14 15 

------ Explanations ------ 

In the test case, M equals to 9.

For C = 1, it's optimal to choose {1} items;

For C = 2, it's optimal to choose {5} items;

For C = 3, it's optimal to choose {1, 5} items;

For C = 4, it's optimal to choose {4, 5} items;

For C = 5, it's optimal to choose {1, 4, 5} items;

For C = 6, it's optimal to choose {3, 4, 5} items;

For C = 7, it's optimal to choose {1, 3, 4, 5} items;

For C = 8, it's optimal to choose {2, 3, 4, 5} items;

For C = 9, it's optimal to choose {1, 2, 3, 4, 5} items.
"""

def calculate_max_costs(N, items):
    ones = []
    twos = []
    
    for W, C in items:
        if W == 1:
            ones.append(C)
        else:
            twos.append(C)
    
    max_weight = len(ones) + 2 * len(twos)
    
    if len(ones) >= 1:
        ones.append(0)
        ones.sort(reverse=True)
        even_twos = twos.copy()
        odd_twos = twos.copy()
        
        for i in range(1, len(ones)):
            if i % 2 == 1:
                even_twos.append(ones[i] + ones[i - 1])
            else:
                odd_twos.append(ones[i] + ones[i - 1])
        
        even_twos = sorted(even_twos)
        odd_twos = sorted(odd_twos)
        
        res = [0, ones[0]]
        for w in range(2, max_weight + 1):
            if w % 2 == 0:
                temp = even_twos.pop()
            else:
                temp = odd_twos.pop()
            res.append(res[w - 2] + temp)
    else:
        res = [0, 0]
        twos = sorted(twos)
        
        for w in range(2, max_weight + 1):
            temp = 0
            if w % 2 == 0:
                temp = twos.pop()
            res.append(max(res[w - 2] + temp, res[w - 1]))
    
    res.pop(0)
    return res