"""
QUESTION:
Give you N cards. Only one natural number is written on each card. However, the same number is never written.

From now on, as a question, I will say an appropriate natural number. Please answer the largest remainder you get when you divide the number on the card you have by the number I said.

For example, suppose you have three cards with 9, 3, and 8, respectively. If I say "4", find the remainder of 9 and 3 and 8 divided by 4, respectively. The remainders are 1, 3, and 0, respectively, but the largest remainder is 3, so 3 is the correct answer.

Let's get started. e? Is it hard to have a lot of cards? It can not be helped. Now let's use the computer to find the largest remainder. Create a program that finds the largest of the remainders of the number on the card divided by the number asked. Ask the question many times, not just once, but never ask the same number more than once.



input

The input consists of one dataset. Input data is given in the following format.


N Q
c1 c2 ... cN
q1
q2
::
qQ


The number of cards N (2 ≤ N ≤ 300000) and the number of questions Q (2 ≤ Q ≤ 100000) are given in the first line, separated by one space, and the number ci (1 ≤ 100000) written on the card in the second line. ci ≤ 300000) is given with one space delimiter. The following Q line is given the number qi (1 ≤ qi ≤ 300000) given as a question.

output

Output the maximum remainder on one line for each question.

Example

Input

3 3
9 3 8
4
6
5


Output

3
3
4
"""

def find_largest_remainder(N, Q, cards, questions):
    tbl = [0] * 300005
    nmax = 0
    tbl[0] = 1
    
    for k in cards:
        tbl[k] = 1
        if k > nmax:
            nmax = k
        tbl[k & 1] = 1
        tbl[k & 3] = 1
        tbl[k & 7] = 1
    
    results = []
    for q in questions:
        if q > nmax:
            results.append(nmax)
        else:
            f = 0
            for k in range(q - 1, -1, -1):
                for i in range(k, nmax + 1, q):
                    if tbl[i]:
                        results.append(k)
                        f = 1
                        break
                if f:
                    break
    
    return results