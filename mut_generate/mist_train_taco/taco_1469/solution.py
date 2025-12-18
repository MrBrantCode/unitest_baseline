"""
QUESTION:
The cloth coasters produced and sold by Aizu Takada City are known for their symmetrical design and great beauty. As part of quality control, Aizu Takada City has installed cameras on the production line to automatically verify that the images obtained by shooting each coaster are symmetrical. Each coaster is represented as a square black and white image of N x N pixels. Each pixel has a value of 0 or 1 corresponding to a white or black image.

This time, the software of the image analysis system will be updated along with the equipment update of the production line. The new system has been devised to reduce the amount of communication data, and data is sent from the camera to the analysis system by the following method.

* The information of the first coaster flowing on the line is sent to the system as an N × N pixel image.
* For the coaster information on the second and subsequent images, only the difference from the previous image is sent. The difference is given as a set of pixel positions that change from "0 to 1" or "1 to 0".



For C coasters, enter the pixel information of the first image and the difference information of the following C-1 image, and create a program that reports the number of coasters that are vertically symmetrical and symmetrical.



Input

The input is given in the following format.


C N
p11p12 ... p1N
p21p22 ... p2N
::
pN1pN2 ... pNN
diff1
diff2
::
diffC-1


The first line gives the number of coasters C (1 ≤ C ≤ 10000) and the number of pixels N (2 ≤ N ≤ 1000 and N is even) in the vertical and horizontal directions of the image. Lines 2 to N + 1 are given the number pij (pij is 0 or 1) in rows N x columns N representing the pixels of the image of the first coaster.

After the N + 2nd line, the difference diffi representing the information of the 2nd and subsequent coasters is given in the following format.


D
r1 c1
r2 c2
::
rD cD


The number of changed pixels D (0 ≤ D ≤ 100) is given in the first line. The following D rows are given ri and ci (1 ≤ ri, ci ≤ N), which represent the row and column numbers of the changed pixels, respectively. The same position cannot be given more than once in diffi.

Output

The number of coasters that are vertically symmetrical and symmetrical is output on one line.

Examples

Input

7 8
00100000
00011000
10111101
01100110
01000110
10111101
00011000
00100100
2
5 3
1 6
1
6 8
3
6 8
3 3
3 6
2
6 3
6 6
0
2
3 8
6 8


Output

3


Input

1 6
000000
000000
010010
010010
000000
000000


Output

1


Input

2 2
00
00
4
1 1
1 2
2 1
2 2


Output

2
"""

def count_symmetrical_coasters(C, N, first_image, diffs):
    def next(N, i):
        return (N - i - 1 + N) % N

    def getState(N, G, i, j):
        return G[i][j] == G[i][next(N, j)] and G[i][j] == G[next(N, i)][j] and (G[i][j] == G[next(N, i)][next(N, j)])

    def getInit(N, G):
        dcnt = 0
        for i in range(N // 2):
            for j in range(N // 2):
                if not getState(N, G, i, j):
                    dcnt += 1
        return dcnt

    G = [row[:] for row in first_image]
    ans = 0
    dcnt = getInit(N, G)
    if dcnt == 0:
        ans += 1

    for diff in diffs:
        k = diff[0]
        changes = diff[1]
        for (r, c) in changes:
            r -= 1
            c -= 1
            pre = getState(N, G, r, c)
            G[r][c] = 0 if G[r][c] == 1 else 1
            post = getState(N, G, r, c)
            if not pre and post:
                dcnt -= 1
            elif pre and not post:
                dcnt += 1
        if dcnt == 0:
            ans += 1

    return ans