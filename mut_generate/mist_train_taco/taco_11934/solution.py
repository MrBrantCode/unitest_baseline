"""
QUESTION:
Santa Claus has Robot which lives on the infinite grid and can move along its lines. He can also, having a sequence of m points p_1, p_2, ..., p_{m} with integer coordinates, do the following: denote its initial location by p_0. First, the robot will move from p_0 to p_1 along one of the shortest paths between them (please notice that since the robot moves only along the grid lines, there can be several shortest paths). Then, after it reaches p_1, it'll move to p_2, again, choosing one of the shortest ways, then to p_3, and so on, until he has visited all points in the given order. Some of the points in the sequence may coincide, in that case Robot will visit that point several times according to the sequence order.

While Santa was away, someone gave a sequence of points to Robot. This sequence is now lost, but Robot saved the protocol of its unit movements. Please, find the minimum possible length of the sequence.


-----Input-----

The first line of input contains the only positive integer n (1 ≤ n ≤ 2·10^5) which equals the number of unit segments the robot traveled. The second line contains the movements protocol, which consists of n letters, each being equal either L, or R, or U, or D. k-th letter stands for the direction which Robot traveled the k-th unit segment in: L means that it moved to the left, R — to the right, U — to the top and D — to the bottom. Have a look at the illustrations for better explanation.


-----Output-----

The only line of input should contain the minimum possible length of the sequence.


-----Examples-----
Input
4
RURD

Output
2

Input
6
RRULDD

Output
2

Input
26
RRRULURURUULULLLDLDDRDRDLD

Output
7

Input
3
RLL

Output
2

Input
4
LRLR

Output
4



-----Note-----

The illustrations to the first three tests are given below.

[Image] [Image] [Image]

The last example illustrates that each point in the sequence should be counted as many times as it is presented in the sequence.
"""

def min_sequence_length(n, movements):
    def correct(p):
        nonlocal typ
        if typ == '':
            typ = p
        elif typ == 'R':
            if p == 'L':
                return False
            if p == 'D' or p == 'U':
                typ = typ + p
        elif typ == 'L':
            if p == 'R':
                return False
            if p == 'D' or p == 'U':
                typ = typ + p
        elif typ == 'U':
            if p == 'D':
                return False
            if p == 'R' or p == 'L':
                typ = typ + p
        elif typ == 'D':
            if p == 'U':
                return False
            if p == 'R' or p == 'L':
                typ = typ + p
        elif typ == 'RU' or typ == 'UR':
            if p != 'R' and p != 'U':
                return False
        elif typ == 'RD' or typ == 'DR':
            if p != 'R' and p != 'D':
                return False
        elif typ == 'LU' or typ == 'UL':
            if p != 'L' and p != 'U':
                return False
        elif typ == 'LD' or typ == 'DL':
            if p != 'L' and p != 'D':
                return False
        return True

    i = 0
    k = 0
    typ = ''
    while i < n:
        while i < n:
            if not correct(movements[i]):
                break
            else:
                i += 1
        k += 1
        typ = ''
    return k