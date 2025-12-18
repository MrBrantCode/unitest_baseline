"""
QUESTION:
This is yet another problem on regular bracket sequences.

A bracket sequence is called regular, if by inserting "+" and "1" into it we get a correct mathematical expression. For example, sequences "(())()", "()" and "(()(()))" are regular, while ")(", "(()" and "(()))(" are not. You have a pattern of a bracket sequence that consists of characters "(", ")" and "?". You have to replace each character "?" with a bracket so, that you get a regular bracket sequence.

For each character "?" the cost of its replacement with "(" and ")" is given. Among all the possible variants your should choose the cheapest.

Input

The first line contains a non-empty pattern of even length, consisting of characters "(", ")" and "?". Its length doesn't exceed 5·104. Then there follow m lines, where m is the number of characters "?" in the pattern. Each line contains two integer numbers ai and bi (1 ≤ ai, bi ≤ 106), where ai is the cost of replacing the i-th character "?" with an opening bracket, and bi — with a closing one.

Output

Print the cost of the optimal regular bracket sequence in the first line, and the required sequence in the second.

Print -1, if there is no answer. If the answer is not unique, print any of them. 

Examples

Input

(??)
1 2
2 8


Output

4
()()
"""

from heapq import heappush, heappop

def find_optimal_bracket_sequence(pattern, costs):
    template = list(pattern)
    n = len(template)
    cost = 0
    balance = 0
    min_heap = []
    
    for i in range(n):
        if template[i] == '(':
            balance += 1
        elif template[i] == ')':
            balance -= 1
        else:
            cost_left, cost_right = costs.pop(0)
            template[i] = ')'
            cost += cost_right
            balance -= 1
            heappush(min_heap, (cost_left - cost_right, i))
        
        if balance < 0:
            if not min_heap:
                return (-1, "")
            change_cost, index = heappop(min_heap)
            template[index] = '('
            cost += change_cost
            balance += 2
    
    if balance == 0:
        return (cost, ''.join(template))
    else:
        return (-1, "")