"""
QUESTION:
problem

There are fine icicles under the eaves of JOI's house in Canada. Because of this, JOI decided to investigate the icicles.

There are N (2 ≤ N ≤ 100000 = 105) icicles under the eaves of JOI's house. These icicles are aligned and i cm (1 ≤ i ≤ N) from the left edge of the eaves. There are i-th icicles at the position of. The length of the i-th icicle is initially ai cm (ai is an integer greater than or equal to 1). These icicles grow according to the following rule:

* The i-th icicles grow by 1 cm per hour only if they are longer than both the i − 1st icicles and the i + 1st icicles (however, consider only one icicle next to one end). That is, the first icicle grows if it is longer than the second icicle, and the Nth icicle grows if it is longer than the N − 1st icicle).
* All icicles break from the root the moment they reach L cm (2 ≤ L ≤ 50000) (the broken icicles are subsequently considered to be 0 cm long icicles).



In the first stage, the lengths of the two adjacent icicles are all different. At this time, if enough time has passed, all N icicles will break to a length of 0 cm. JOI, I wanted to know how long it would take for the icicles to reach this state.

Given the initial length of N icicles and the limit length L of the icicles, write a program that finds the time it takes for all the icicles to break.

output

The output consists of one line containing only one integer that represents the time it takes for all the icicles to break.

Input / output example

Input example 1


4 6
Four
2
3
Five


Output example 1


8


In the case of Example 1, the 1, 2, 3, and 4 icicles break after 2, 8, 4, and 1 hour, respectively. Therefore, it takes 8 hours for all the icicles to break. Output 8.




Input example 2


6 10
3
Four
1
9
Five
1


Output example 2


15


The above question sentences and the data used for the automatic referee are the question sentences created and published by the Japan Committee for Information Olympics and the test data for scoring.



input

On the first line of the input, the integer N, which represents the number of icicles, and the integer L, which represents the limit length of the icicles, are written in this order, separated by blanks. Input i + line 1 (1 ≤ i) In ≤ N), the integer ai (1 ≤ ai <L) representing the first length of the i-th icicle is written.

Of the scoring data, 30% of the points are N ≤ 500 and L ≤ 1000.

Example

Input

4 6
4
2
3
5


Output

8
"""

def calculate_icicle_break_time(icicles, L):
    N = len(icicles)
    
    def calcDiff(icicles, N):
        diff_2times = [0] * N
        for idx in range(N):
            dif_right = icicles[idx + 1] - icicles[idx] if idx != N - 1 else -icicles[idx]
            dif_left = icicles[idx] - icicles[idx - 1] if idx != 0 else icicles[idx]
            dif_right = 1 if dif_right > 0 else -1
            dif_left = 1 if dif_left > 0 else -1
            if dif_right - dif_left < 0:
                diff_2times[idx] = -1
            elif dif_right - dif_left > 0:
                diff_2times[idx] = 1
            else:
                diff_2times[idx] = 0
        return diff_2times
    
    diff_2times = calcDiff(icicles, N)
    time = [-1] * N
    peakX = [i for i in range(N) if diff_2times[i] == -1]
    
    for i in peakX:
        time[i] = L - icicles[i]
        (isLocalMinL, isLocalMinR) = (False, False)
        (posL, posR) = (i, i)
        while not (isLocalMinL and isLocalMinR):
            posL -= 1
            if posL < 0:
                isLocalMinL = True
            if not isLocalMinL:
                if time[posL] == -1:
                    time[posL] = L - icicles[posL] + time[posL + 1]
                else:
                    time[posL] = L - icicles[posL] + max(time[posL - 1], time[posL + 1])
                if diff_2times[posL] == 1:
                    isLocalMinL = True
            posR += 1
            if posR >= N:
                isLocalMinR = True
            if not isLocalMinR:
                if time[posR] == -1:
                    time[posR] = L - icicles[posR] + time[posR - 1]
                else:
                    time[posR] = L - icicles[posR] + max(time[posR - 1], time[posR + 1])
                if diff_2times[posR] == 1:
                    isLocalMinR = True
    
    return max(time)