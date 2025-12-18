"""
QUESTION:
Given a number of friends who have to give or take some amount of money from one another. Design an algorithm by which the total cash flow among all the friends is minimized. 
Example 1:
Input:
N=3
transaction [][]={{0,100,0}, {0,0,100}, {100,0,0}}
Output:
transaction [][]={{0,0,0},{0,0,0},{0,0,0}}
Explanation:
Since friend one has to give friend two which has to give friend three and which in turn has to give one. So it is better than no one will do anything to anyone.
Example 2:
Input:
N=3
transaction [][]={{0,100,0{,{0,0,200},{0,0,0}}
Output:
transaction [][]={0,0,100},{0,0,100},{0,0,0}
Explanation:
The net flow is minimized.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minCashFlow() which takes the transaction array and number of friends as input parameters and returns the new transaction array as output;.
 
 
Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(N*N)
 
Constraints:
1 <= N <= 1000
0^{ }<= transactio[i][j] <= 1000
"""

from typing import List

def min_cash_flow(n: int, transaction: List[List[int]]) -> List[List[int]]:
    optArr = [[0 for _ in range(n)] for _ in range(n)]
    graph = [[] for _ in range(n)]
    amounts = [0 for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if transaction[i][j]:
                graph[i].append([j, transaction[i][j]])
    
    for i in range(n):
        curLen = len(graph[i])
        for j in range(curLen):
            amounts[i] -= graph[i][j][1]
            amounts[graph[i][j][0]] += graph[i][j][1]
    
    while True:
        maxCredit = 0
        maxDebit = 0
        ci = None
        di = None
        
        for i in range(n):
            if amounts[i] > maxCredit:
                ci = i
                maxCredit = amounts[i]
            if amounts[i] < maxDebit:
                di = i
                maxDebit = amounts[i]
        
        if maxCredit == 0 and maxDebit == 0:
            break
        
        if maxCredit >= abs(maxDebit):
            optArr[di][ci] = abs(maxDebit)
            amounts[di] = 0
            amounts[ci] -= abs(maxDebit)
        else:
            optArr[di][ci] = maxCredit
            amounts[di] += maxCredit
            amounts[ci] = 0
    
    return optArr