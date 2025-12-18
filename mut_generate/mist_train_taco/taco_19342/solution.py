"""
QUESTION:
An employee's wallet can contain no more than M notes or coins. A boss pays his salary by the minimum notes possible. However the employee may have to leave out some money. Find how much money he has to lose if his original salary is N.
Note: The values of notes or coins available are 1000, 500, 100, 50, 20, 10, 5, 2 and 1.
Example 1:
Input:
N = 1712, M = 4
Output:
12
Explanation:
The boss will give him one 1000, one 500
and two 100 notes, one note of 10 and
one of 2. But because the employee can't
have more notes than 4, he can have a
maximum amount of 1700.
So, he will lose 12.
Example 2:
Input:
N = 1023, M = 2
Output:
3
Explanation:
The boss will give him one 1000, one 20
one 2 and one note of 1. But because the
employee can't have more notes than 2,
he can have a maximum amount of 1020.
So, he will lose 3.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getLoss() which takes 2 Integers N and M as input and returns the answer.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N,M <= 10^{5}
"""

def calculate_loss(N, M):
    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    count = 0
    i = 0
    while count < M and N > 0:
        if N >= notes[i]:
            N -= notes[i]
            count += 1
        else:
            i += 1
    return N