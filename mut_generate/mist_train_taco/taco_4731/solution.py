"""
QUESTION:
Indraneel's student has given him data from two sets of experiments that the student has performed. Indraneel wants to establish a correlation between the two sets of data. Each data set is a sequence of $N$ numbers. The two data sets do not match number for number, but Indraneel believes that this is because data has been shifted due to inexact tuning of the equipment.
For example, consider the following two sequences:
$ $
3  8   4  23  9  11  28
2  3  22  26  8  16  12

$ $
Indraneel observes that if we consider the subsequences $3,4,23,9$ and $2,3,22,8$ and examine their successive differences we get $1,19,-14$. He considers these two subsequences to be "identical". He would like to find the longest such pair of subsequences so that the successive differences are identical. Your task is to help him do this.

-----Input:-----
The first line of the input will contain a single integer $N$ indicating the number of data points in each of Indraneel's student's data sets. This is followed by two lines, each containing $N$ integers.

-----Output:-----
The output consists of three lines. The first line of output contains a single integer indicating the length of the longest pair of subsequences (one from each sequence) that has identical successive differences. This is followed by two lines each containing the corresponding subsequences. If there is more than one answer, it suffices to print one.

-----Constraints:-----
- $1 \leq N \leq 150$.
- $0 \leq$ Each data point $\leq 1000$

-----Sample Input-----
7
3 8 4 23 9 11 28  
2 3 22 26 8 16 12 

-----Sample Output-----
4
3 4 23 9
2 3 22 8
"""

import copy

def find_longest_identical_subsequences(a, b):
    n = len(a)
    ma = -10 ** 9
    p1 = []
    p2 = []
    
    def lcsfn(a, c, corda, cordb):
        d = []
        lcs = []
        for i in range(n + 1):
            d.append([0] * (n + 1))
            lcs.append([0] * (n + 1))
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if a[i - 1] == c[j - 1]:
                    lcs[i][j] = lcs[i - 1][j - 1] + 1
                    d[i][j] = 'd'
                elif lcs[i - 1][j] > lcs[i][j - 1]:
                    lcs[i][j] = lcs[i - 1][j]
                    d[i][j] = 'u'
                else:
                    lcs[i][j] = lcs[i][j - 1]
                    d[i][j] = 'l'
        i = n
        j = n
        cost = 0
        while i >= 1 and j >= 1:
            if d[i][j] == 'd':
                corda.append(a[i - 1])
                cordb.append(b[j - 1])
                i -= 1
                j -= 1
                cost += 1
            elif d[i][j] == 'l':
                j -= 1
            elif d[i][j] == 'u':
                i -= 1
        return cost
    
    for i in range(-1000, 1001):
        c = []
        corda = []
        cordb = []
        for j in range(n):
            c.append(b[j] + i)
        p = lcsfn(a, c, corda, cordb)
        if ma < p:
            ma = p
            p1 = copy.deepcopy(corda)
            p1 = p1[::-1]
            p2 = copy.deepcopy(cordb)
            p2 = p2[::-1]
    
    return ma, p1, p2