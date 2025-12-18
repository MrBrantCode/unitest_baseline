"""
QUESTION:
problem

Play by arranging white and black stones on the table. First, place the stones on the left edge of the table. Then place the stones in the second place from the left. Repeat this n times to arrange n stones in a horizontal row. However, when placing a new i-th go stone, replace the go stone on the table according to the following rules.

* If i is odd: Do not replace the stones that were on the table, but place the new stones i-th from the left.
* If i is even: If the color of the new go stone placed i-th from the left and the color of the rightmost go stone on the table are the same, the go stone on the table is not replaced and the new go stone is placed i-th from the left. If this is not the case, that is, if the color of the new i-th go stone from the left is different from the color of the right-most go stone on the table, first remove all the consecutive right-end go stones of the same color on the table, and then use the i-th go stone. Replace with a go stone of the same color, and place the i-th go stone on the right edge of the table.



For example, when the first 7 go stones are placed,

○○ ●● ○○○

(○ represents white go stones, ● represents black go stones.)

* If the 8th go stone is white (○), it is the same color as the rightmost go stone, so leave it as it is. Therefore, the go stone on the table is


○○ ●● ○○○○

Will be.
* If the 8th go stone is black (●), the color is different from the rightmost go stone (○), so first remove the 3 consecutive white go stones (○) on the right end of the table, and then remove the black go stone (●). And put the eighth go stone on the far right. Therefore, the go stone on the table


○○ ●●●●●●

Will be.



Given the order of the stones to be placed as input, create a program to find the number of white stones placed on the table after arranging n stones.



input

The input consists of multiple datasets. Each dataset is given in the following format.

A positive integer n (1 ≤ n ≤ 100000) is written on the first line. In the second and subsequent lines i + 1 (1 ≤ i ≤ n), the color of the go stone placed in the i-th position is written. The integer ci is written, and if ci is 0, it means that the color of the i-th go stone is white, and if it is 1, it means that the color of the i-th go stone is black.

Of the scoring data, 50% of the points are given by satisfying n ≤ 10000.

When n is 0, it indicates the end of input. The number of datasets does not exceed 10.

output

For each dataset, output the number of white stones placed on the table after arranging n stones in one line.

Examples

Input

8
1
0
1
1
0
0
0
0
8
1
0
1
1
0
0
0
1
0


Output

6
2


Input

None


Output

None
"""

def count_white_stones(n, stones):
    if n == 0:
        return 0
    
    edge = stones[0]
    sq = 0
    past = []
    
    for i in range(n):
        nxt = stones[i]
        if i % 2 == 0:
            if nxt == edge:
                sq += 1
            else:
                edge = nxt
                past.append(sq)
                sq = 1
        elif nxt == edge:
            sq += 1
        else:
            edge = nxt
            sq += 1
            if past:
                sq += past.pop()
    
    past.append(sq)
    answer = 0
    
    for i in range(len(past)):
        if edge == 0:
            answer += past[-i - 1]
        edge = 1 - edge
    
    return answer