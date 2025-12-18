"""
QUESTION:
Illumination

Illuminations are displayed in the corridors every year at the JOI High School Cultural Festival. The illuminations consist of N light bulbs, which are lined up in a row from the west side to the east side of the corridor. Each light bulb is either on or off.

A machine that operates a light bulb is sleeping in the warehouse of JOI High School. When a continuous light bulb is specified in the illumination, this machine turns all the specified light bulbs with the light on and all the light bulbs without the light on. However, the machine is aging and can only be used once.

JOI high school students like alternating rows of light bulbs with and without lights (such rows of light bulbs are called alternating rows). Therefore, I decided to use this machine only once if necessary to make illuminations containing alternating rows as long as possible.

Example

For example, the arrangement of illuminations is from west to east

<image>



(○ indicates a light bulb with a light, ● indicates a light bulb without a light). At this time, if you operate the machine for the four light bulbs from the 4th to the 7th,

<image>



The second to eighth bulbs form an alternating row of length 7.

<image>



Also, if you operate the machine only for the 8th light bulb,

<image>



The 4th to 10th light bulbs form an alternating row of length 7.

<image>



It is not possible to create alternating rows longer than 8 by using the machine up to once.

Task

Given the illumination information, write a program to find the maximum possible length of the alternating rows in the array of light bulbs that can be obtained by using the machine up to once.

Limits

* 2 ≤ N ≤ 100 000 Number of light bulbs that make up the illumination



input

Read the following data from standard input.

* The integer N is written on the first line.
* On the second line, N 0s or 1s are written with a space as a delimiter. Each integer represents the information of the light bulb before operating the machine. The i (1 ≤ i ≤ N) th integer from the left represents the information of the i-th light bulb from the west, and if the integer is 1, the light bulb is on, and if it is 0, the light bulb is off.



output

Output an integer representing the maximum length of the alternating columns contained in the columns of light bulbs that can be created to the standard output on one line.

Input / output example

Input example 1


Ten
1 1 0 0 1 0 1 1 1 0


Output example 1


7


This is an example explained in the problem statement.




Input example 2


Ten
1 0 0 0 0 1 0 1 0 1


Output example 2


8


Manipulating only the fourth bulb from the west yields an alternating sequence that satisfies the maximum value of 8.




Input example 3


Five
1 1 0 1 1


Output example 3


Five


By manipulating the second to fourth light bulbs counting from the west, you can create an alternating row of all light bulbs.




Input example 4


3
0 1 0


Output example 4


3


Note that you may not need to use a machine.

The question text and the data used for the automatic referee are the question text and the test data for scoring, which are created and published by the Japan Committee for Information Olympics.





Example

Input

10
1 1 0 0 1 0 1 1 1 0


Output

7
"""

def max_alternating_length(N, A):
    # Step 1: Modify the array to simulate the effect of the machine
    for i in range(N):
        A[i] ^= i & 1
    
    # Step 2: Count consecutive segments of the same value
    B = []
    prev = A[0]
    cnt = 0
    for i in range(N):
        if prev != A[i]:
            B.append(cnt)
            cnt = 1
        else:
            cnt += 1
        prev = A[i]
    B.append(cnt)
    
    # Step 3: Calculate the maximum length of alternating segments
    if len(B) == 1:
        return B[0]
    elif len(B) == 2:
        return B[0] + B[1]
    else:
        return max((B[i] + B[i + 1] + B[i + 2] for i in range(len(B) - 2)))