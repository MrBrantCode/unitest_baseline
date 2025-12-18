"""
QUESTION:
An art exhibition will be held in JOI. At the art exhibition, various works of art from all over the country will be exhibited.

N works of art were collected as candidates for the works of art to be exhibited. These works of art are numbered 1, 2, ..., N. Each work of art has a set value called size and value. The size of the work of art i (1 \ leq i \ leq N) is A_i, and the value is B_i.

At the art exhibition, one or more of these works of art will be selected and exhibited. The venue for the art exhibition is large enough to display all N works of art. However, due to the aesthetic sense of the people of JOI, I would like to select works of art to be exhibited so that the size difference between the works of art does not become too large. On the other hand, I would like to exhibit as many works of art as possible. Therefore, I decided to select the works of art to be exhibited so as to meet the following conditions:

* Let A_ {max} be the size of the largest piece of art and A_ {min} be the size of the smallest piece of art selected. Also, let S be the sum of the values ​​of the selected works of art.
* At this time, maximize S-(A_ {max} --A_ {min}).



Task

Given the number of candidates for the works of art to be exhibited and the size and value of each work of art, find the maximum value of S-(A_ {max} --A_ {min}).

input

Read the following input from standard input.

* The integer N is written on the first line. This represents the number of candidates for the works of art to be exhibited.
* In the i-th line (1 \ leq i \ leq N) of the following N lines, two integers A_i and B_i are written separated by a blank. These indicate that the size of the work of art i is A_i and the value is B_i.


output

Output the maximum value of S-(A_ {max} --A_ {min}) to the standard output on one line.

Limits

All input data satisfy the following conditions.

* 2 \ leq N \ leq 500 000.
* 1 \ leq A_i \ leq 1 000 000 000 000 000 = 10 ^ {15} (1 \ leq i \ leq N).
* 1 \ leq B_i \ leq 1 000 000 000 (1 \ leq i \ leq N).



Input / output example

Input example 1


3
twenty three
11 2
4 5


Output example 1


6


In this input example, there are three candidates for the works of art to be exhibited. The size and value of each work of art are as follows.

* The size of art 1 is 2 and the value is 3.
* Art 2 has a size of 11 and a value of 2.
* Art 3 has a size of 4 and a value of 5.



In this case, if you choose to display art 1 and art 3, then S-(A_ {max} --A_ {min}) = 6 as follows.

* The largest work of art selected is work of art 3. Therefore, A_ {max} = 4.
* The smallest work of art selected is work of art 1. Therefore, A_ {min} = 2.
* Since the sum of the values ​​of the selected works of art is 3 + 5 = 8, S = 8.



Since it is impossible to set S-(A_ {max} --A_ {min}) to 7 or more, 6 is output.

Input example 2


6
4 1
1 5
10 3
9 1
4 2
5 3


Output example 2


7


Input example 3


15
1543361732 260774320
2089759661 257198921
1555665663 389548466
4133306295 296394520
2596448427 301103944
1701413087 274491541
2347488426 912791996
2133012079 444074242
2659886224 656957044
1345396764 259870638
2671164286 233246973
2791812672 585862344
2996614635 91065315
971304780 488995617
1523452673 988137562


Output example 3


4232545716





Creative Commons License
Information Olympics Japan Committee work "17th Japan Information Olympics (JOI 2017/2018) Final Selection"





Example

Input

3
2 3
11 2
4 5


Output

6
"""

def maximize_art_exhibition_value(N, art_works):
    # Sort the art works based on their sizes
    art_works.sort()
    
    # Initialize variables
    su = 0
    S = -art_works[0][0]
    ans = -10 ** 19
    
    # Iterate through the sorted art works
    for a, b in art_works:
        S = min(S, su - a)
        ans = max(ans, su + b - a - S)
        su += b
    
    return ans