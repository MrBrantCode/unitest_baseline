"""
QUESTION:
Chef is playing with an expression which consists of integer operands and the following binary
Bitwise operators -  AND, OR and XOR. He is trying to figure out that what could be the Maximum possible answer of the expression, given that he can perform the operation in any order i.e not necessarily follow the rule of Precedence of operators while evaluating the expression.
After some time of consistent work Chef starts feeling exhausted and wants you to automate this process for him. Can you help him out?
The expression has Bitwise operators in symbol format:
- &  stands for AND 
- |   stands for OR
- ^   stands for XOR
NOTE : It is guaranteed that the expression will always be valid, also each OPERATOR will always be preceded and succeeded by an OPERAND.

-----Input:-----
- The first line of input contains a single integer $T$ denoting the number of test cases.
- The only line of input for each test case is a $string$ which is the Chef's expression to evaluate.

-----Output:-----
For each test case print a single integer i.e the maximum possible value of Chef's expression.

-----Constraints-----
- $1 \leq T \leq 100$.
- The number of OPERATORS in the expression will be atleast 1 and atmost 10.
- Each OPERAND may range from 0 to $10^9$.

-----Subtasks-----
- 10 points : The number of OPERATORS in the expression will be atmost 5.
- 20 points : The number of OPERATORS in the expression will be atmost 8.
- 70 points : Original constraints.

-----Sample Input:-----
2
3^40|10^2

92^95|56&2&3

-----Sample Output:-----
43

95

-----EXPLANATION:-----CASE 2 :
- If we first compute (56 & 2), the expression becomes 92^95|0&3, since (56 & 2) yields $0$.
- Now on computing (95 | 0), the expression becomes 92^95&3.
- Further on computing (95 & 3), the expression becomes 92^3.
- Finally (92 ^ 3) yields 95, which is the maximum value of the expression.
"""

def max_expression_value(expression: str) -> int:
    def value(a, b, c):
        if c == '&':
            return a & b
        elif c == '^':
            return a ^ b
        elif c == '|':
            return a | b
        return 0  # Default case, should never be reached

    def break_rules(n, operator):
        if len(n) == 1:
            return n
        elif len(n) == 2:
            return [value(n[0], n[1], operator[0])]
        else:
            cont_ans = []
            for i in range(1, len(n)):
                l1 = n[:i]
                l2 = n[i:]
                o1 = operator[:i - 1]
                o2 = operator[i:]
                l1_ans = break_rules(l1, o1)
                l2_ans = break_rules(l2, o2)
                for k in l1_ans:
                    for j in l2_ans:
                        cont_ans.append(value(k, j, operator[i - 1]))
            return cont_ans

    operator = []
    num = []
    temp = ''
    for i in range(len(expression)):
        if ord(expression[i]) > 47 and ord(expression[i]) < 58:
            temp = temp + expression[i]
        else:
            num.append(int(temp))
            temp = ''
            operator.append(expression[i])
        if i == len(expression) - 1:
            num.append(int(temp))

    return max(break_rules(num, operator))