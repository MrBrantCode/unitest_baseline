"""
QUESTION:
problem

The JOI country has one long enough road running east to west. The royal palace of JOI country is along the road, and the position along the road in JOI country is represented by the integer A. When A = 0, it represents the position of the royal palace. When A> 0, it indicates the position A meters east of the royal palace. When A <0, it represents a position that is -A meters west of the royal palace.

There are N houses along the roads in JOI, and the houses are numbered from 1 to N in order from the west. There are N people in JOI country, and the people are numbered from 1 to N. The people i live in the house i. The position of house i is represented by a non-zero even Ai. A1, ..., AN are all different.

In JOI country, the lack of movement of the people has become a problem in recent years. The King of JOI, who was concerned about the health of the people, ordered all the people to take a walk. When the King gives an order, all the people start walking eastward or westward all at once. The direction in which each nation starts walking is determined by each nation. All people walk at a speed of 1 meter per second when walking.

All the people of JOI love to talk. If you meet other people during your walk, you will stop there and start small talk. The same is true if you meet a people who have already stopped. The people who have stopped once will not start walking again.

There are Q important people in JOI country. The King of JOI wants to know the position of Q important persons T seconds after the order is issued. Create a program to find the position of Q important persons T seconds after the command is issued.

input

The input consists of 1 + N + Q lines.

On the first line, three integers N, T, Q (1 ≤ N ≤ 100000 (= 105), 0 ≤ T ≤ 1018, 1 ≤ Q ≤ 1000, 1 ≤ Q ≤ N) are written separated by blanks. ing. This means that there are N houses in JOI country, and we want to know the position of Q important people T seconds after the king issues the order.

Two integers Ai and Di (-1018 ≤ Ai ≤ 1018, Ai is a non-zero even number, 1 ≤ Di ≤ 2) are written on the i-th line of the following N lines, separated by blanks. Ai is an even number representing the position of house i. For all i (1 ≤ i ≤ N-1), Ai <Ai + 1 is satisfied. Di indicates the direction in which the national i starts walking after the command is issued. When Di = 1, national i starts walking eastward. When Di = 2, national i starts walking westward.

The integer Xi (1 ≤ Xi ≤ N) is written on the i-th line of the following Q lines. This means that the i-th important person lives in the house Xi. For all i (1 ≤ i ≤ Q-1), Xi <Xi + 1 is satisfied.

Of the five input data given, input 1 satisfies N ≤ 100 and T ≤ 10000. In addition, input 2 satisfies N ≤ 5000. Also, at input 3, there is a certain integer M (1 ≤ M ≤ N-1), Di = 1 for all i (1 ≤ i ≤ M), and for all j (M + 1 ≤ j ≤ N). Satisfy Dj = 2. Also, for inputs 1, 2, and 3, the absolute value of the integer given to the input does not exceed 1000000000 (= 109). Note that for inputs 4 and 5, the given integer does not fall within the range of 32-bit signed integers.

output

The output consists of Q lines.

On line i (1 ≤ i ≤ Q), output an integer representing the position of the i-th important person T seconds after the King issued the command. It is guaranteed that this value is an integer from the condition of the problem statement.

Input / output example

Input example 1


5 5 3
-8 1
-4 2
-twenty two
4 2
10 1
1
3
Five


Output example 1


-6
-6
15


Input example 2


7 18 5
-100 1
-56 2
-34 1
-30 1
-22 1
-4 2
18 2
1
3
Four
Five
7


Output example 2


-82
-16
-13
-13
0


Creative Commons License

Information Olympics Japan Committee work "15th Japan Information Olympics JOI 2015/2016 Qualifying Competition Tasks"





Example

Input

5 5 3
-8 1
-4 2
-2 2
4 2
10 1
1
3
5


Output

-6
-6
15
"""

def calculate_final_positions(N, T, Q, positions_and_directions, important_people_indices):
    R = {}
    A = []
    B = []
    prv = 1

    for (x, t) in positions_and_directions:
        if prv == t:
            if t == 1:
                A.append(x)
            else:
                B.append(x)
        elif prv == 2:
            y = (A[-1] if A else -10 ** 19) + (B[0] if B else 10 ** 19) >> 1
            for z in A:
                R[z] = min(z + T, y)
            for z in B:
                R[z] = max(z - T, y)
            A = [x]
            B = []
        else:
            B.append(x)
        prv = t

    if A or B:
        y = (A[-1] if A else -10 ** 19) + (B[0] if B else 10 ** 19) >> 1
        for z in A:
            R[z] = min(z + T, y)
        for z in B:
            R[z] = max(z - T, y)

    final_positions = [R[positions_and_directions[i - 1][0]] for i in important_people_indices]
    return final_positions