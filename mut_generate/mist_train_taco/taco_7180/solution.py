"""
QUESTION:
Oh, no!

The coronavirus has caught you, and now you're sitting in a dark cellar, with tied legs (but not hands). You have a delicious cookie, a laptop in front of you, and your ideal development environment is open. The coronavirus convinces you to solve the following problem.

You are given two arrays A and B of size n. You can do operations of two types with array A: 

  * Reverse array A. That is the array [A_1,\ A_2,\ …,\ A_n] transformes into [A_n,\ A_{n-1},\ …,\ A_1]. 
  * Replace A with an array of its prefix sums. That is, the array [A_1,\ A_2,\ …,\ A_n] goes to [A_1,\ (A_1+A_2),\ …,\ (A_1+A_2+…+A_n)]. 



You need to understand if you can get an array B from the array A. If it is possible, you will have to restore the order of these operations by minimizing the number of operations of the second type. Fortunately, the coronavirus is good today, so he has allowed you not to restore actions if the minimum number of second type operations is more than 2⋅ 10^5. But coronavirus resents you, so if you restore the answer, the total number of operations should not exceed 5⋅ 10^5.

Solve this problem and get the cookie, or the coronavirus will extend the quarantine for five years and make the whole economy collapse! 

Input

The first line contains a single integer n (1≤ n ≤ 2⋅ 10^5).

The second line contains n integers A_1, A_2, …, A_n (1 ≤ A_i ≤ 10 ^ {12}).

The third line contains n integers B_1, B_2, …, B_n (1 ≤ B_i ≤ 10 ^ {12}).

Output

If you cannot get B from the A array, print "IMPOSSIBLE" (without quotes) on a single line.

If the minimum number of operations of the second type exceeds 2⋅ 10^5, print "BIG" (without quotes). In the second line print the number of operations of the second type, that needs to be applied to get array B from A.

Otherwise, in the first line print "SMALL" (without quotes). In the second line print the total number of operations of the first and second types m ≤ 5⋅ 10^5 (it is guaranteed that in this case there is such a sequence of actions). In the third line print a line of length m, consisting of characters 'R"and 'P' (without quotes).

The i-th character should be 'R', if the i-th action is of the first type, and should be 'P', otherwise.

If there are several such sequences, you can print any of them.

You can print each character in the uppercase or in the lowercase.

Examples

Input


2
5 7
5 7


Output


SMALL
0



Input


2
1 1
300000 1


Output


BIG
299999


Input


2
10 1
13 14


Output


SMALL
6
RPPPRP


Input


3
1 2 1
2 1 2


Output


IMPOSSIBLE

Note

In the first example, the arrays A and B already equal, so the number of required operations =0.

In the second example, we need to replace A with the prefix sums 299999 times and then reverse the array. Since 299999>2⋅ 10^5, there is no need to restore the answer.

In the fourth example, you cannot get B from the A.
"""

def can_transform_arrays(n, A, B):
    def reverse_array(arr):
        return arr[::-1]
    
    def prefix_sum_array(arr):
        return [sum(arr[:i+1]) for i in range(len(arr))]
    
    if n == 1:
        if A == B:
            return "SMALL", 0, ""
        else:
            return "IMPOSSIBLE"
    
    if n == 2:
        mna = min(A)
        cntp = 0
        x, y = B
        if x > y:
            x, y = y, x
        while mna < x:
            c = y // x
            cntp += c
            y -= c * x
            if x > y:
                x, y = y, x
        d = y - max(A)
        if mna != x or d % x:
            return "IMPOSSIBLE"
        cntp += d // x
        if cntp > 200000:
            return "BIG", cntp
    
    ans = ''
    cntp = 0
    raa = reverse_array(A)
    
    while True:
        if A == B:
            if cntp > 200000:
                return "BIG", cntp
            else:
                return "SMALL", len(ans), ans[::-1] if ans else ""
        if raa == B:
            if cntp > 200000:
                return "BIG", cntp
            else:
                ans += 'R'
                return "SMALL", len(ans), ans[::-1] if ans else ""
        if B[0] <= B[-1]:
            if cntp <= 200000:
                ans += 'P'
            cntp += 1
            for i in range(n - 2, -1, -1):
                B[i + 1] -= B[i]
                if B[i + 1] <= 0:
                    return "IMPOSSIBLE"
        else:
            if cntp <= 200000:
                ans += 'R'
            B = reverse_array(B)