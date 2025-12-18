"""
QUESTION:
problem

You are playing with J using the Midakuji. The Amida lottery consists of n vertical bars and m horizontal bars. The vertical bars are numbered from 1 to n in order from the left, and the vertical bar i The positive integer si is written at the bottom of.

<image>

Figure 3-1 Example of Amidakuji (n = 4, m = 5, s1 = 20, s2 = 80, s3 = 100, s4 = 50)

The integer written at the bottom of the vertical bar i, which is reached by following the path from the top of the vertical bar i, is the score when the vertical bar i is selected. For example, in Fig. 3-1 the vertical bar 1 is selected. And the score is 80 points, and if the vertical bar 2 is selected, the score is 100 points.

<image>

Figure 3-2 Example of how to follow the road

Mr. J decides to choose a series of k books from vertical bar 1 to vertical bar k. The total score when selecting those k vertical bars is J's score. However, you are in the Amidakuji You can select one horizontal bar and delete that horizontal bar from the Amidakuji. (You do not have to delete it.) If you delete one horizontal bar, the vertical bar in the deleted Amidakuji will be displayed vertically. J's score is the total of the points when selecting k consecutive vertical bars from bar 1 to vertical bar k.

Given the shape of the Amida lottery and the number of vertical bars k that J chooses as input, create a program that finds the minimum value of J's score.



input

The input consists of multiple datasets. Each dataset is given in the following format.

On the first line, four integers n, m, h, k are written separated by blanks. N (2 ≤ n ≤ 1000) is the number of vertical bars, and m (1 ≤ m ≤ 100000) is the horizontal bar. H (2 ≤ h ≤ 1000) represents the length of the vertical bar, and k (1 ≤ k ≤ n) represents the number of vertical bars you choose.

The following n lines contain the score written at the bottom of the vertical bar. The first line (1 ≤ i ≤ n) contains the positive integer si. Also, s1 + s2 + ... + sn ≤ 2000000000 = 2 × 109.

The following m lines indicate the position of the horizontal bar. The horizontal bars are numbered from 1 to m. The first line (1 ≤ i ≤ m) is the horizontal bar i. The two integers ai, bi (1 ≤ ai ≤ n --1, 1 ≤ bi ≤ h --1) representing the position are separated by blanks, and the horizontal bar i connects the vertical bar ai and the vertical bar ai + 1. , Indicates that the distance from the top edge of the horizontal bar i is bi. However, no two horizontal bars share an endpoint.

Of the scoring data, 20% of the points will have the lowest score for Mr. J if the horizontal bar is not deleted. Also, 30% of the points will satisfy n ≤ 20, m ≤ 30, h ≤ 10. 60% of the points are m ≤ 1000.

The end of the input is indicated by a line containing four zeros. The number of datasets does not exceed 10.

output

For each dataset, output the minimum score of Mr. J on one line.

Examples

Input

4 5 7 2
20
80
100
50
1 1
2 6
2 3
1 5
3 1
2 2 5 1
10
20
1 1
1 3
0 0 0 0


Output

100
10


Input

None


Output

None
"""

def calculate_minimum_score(n, m, h, k, scores, horizontal_bars):
    i_lst = [i for i in range(n)]
    b_lst = sorted(horizontal_bars, key=lambda x: x[1])
    pare_lst = []
    
    for bar in b_lst:
        ind = bar[0]
        temp = i_lst[ind]
        i_lst[ind] = i_lst[ind - 1]
        i_lst[ind - 1] = temp
        pare_lst.append((i_lst[ind], i_lst[ind - 1]))
    
    new_s_lst = [0] * n
    for i in range(n):
        new_s_lst[i_lst[i]] = scores[i]
    
    ans = sum(new_s_lst[:k])
    max_dec = 0
    
    for pare in pare_lst:
        a = pare[0]
        b = pare[1]
        if a < k and b >= k and (new_s_lst[a] - new_s_lst[b] > max_dec):
            max_dec = new_s_lst[a] - new_s_lst[b]
        if b < k and a >= k and (new_s_lst[b] - new_s_lst[a] > max_dec):
            max_dec = new_s_lst[b] - new_s_lst[a]
    
    return ans - max_dec