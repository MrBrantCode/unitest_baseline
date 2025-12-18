"""
QUESTION:
<image>


There is a container that is bifurcated as shown in the figure. Drop 10 balls numbered from 1 to 10 through the opening A of the container and place the balls in the left cylinder B or the right cylinder C. Since plate D can rotate left and right around the fulcrum E, you can move plate D to decide whether to put it in cylinder B or cylinder C.

Gives a sequence of balls to drop from opening A. Put them in cylinder B or cylinder C in order. At this time, create a program that outputs YES if both cylinder B and cylinder C can arrange large balls on the small numbered balls, and NO if they cannot be arranged. However, the order of the balls cannot be changed in the container. In addition, it is assumed that they can be put in the same cylinder in succession, and that there is enough room for all 10 balls in both cylinders B and C.



Input

Given multiple datasets. The number of datasets N is given in the first line. Then you are given a dataset of N rows. Each dataset is given 10 numbers, starting from the left, separated by blanks.

Output

Print YES or NO on one line for each dataset.

Example

Input

2
3 1 4 2 5 6 7 8 9 10
10 9 8 7 6 5 4 3 2 1


Output

YES
NO
"""

def can_arrange_balls(datasets):
    results = []
    
    for balls in datasets:
        left = [0]
        right = [0]
        m = 0
        
        while True:
            if m == 10:
                results.append('YES')
                break
            if balls[m] < left[-1] and balls[m] < right[-1]:
                results.append('NO')
                break
            if balls[m] > left[-1] and balls[m] > right[-1]:
                if left[-1] > right[-1]:
                    left.append(balls[m])
                else:
                    right.append(balls[m])
            elif balls[m] > left[-1]:
                left.append(balls[m])
            else:
                right.append(balls[m])
            m += 1
    
    return results