"""
QUESTION:
The following sorting operation is repeated for the stacked blocks as shown in Fig. A.

1. Stack all the bottom blocks (white blocks in Figure a) on the right edge (the remaining blocks will automatically drop one step down, as shown in Figure b).
2. If there is a gap between the blocks, pack it to the left to eliminate the gap (from Fig. B to Fig. C).



For an integer k greater than or equal to 1, a number represented by k × (k + 1) / 2 (example: 1, 3, 6, 10, ...) is called a triangular number. If the total number of blocks is a triangular number, it is expected that if the above sorting is repeated, the height of the left end will be 1 and the total number will increase by 1 toward the right (Fig. D shows the total number). For 15).

<image>


When the first sequence of blocks is given, when the triangle of the block as explained above is created by the operation less than the predetermined number of times, create a program that outputs the minimum number of operations until the triangle is obtained. please.



input

The input consists of multiple datasets. The end of the input is indicated by a single zero line. Each dataset is given in the following format.


N
b1 b2 ... bN


Each dataset has two rows and represents the first sequence of blocks. N (1 ≤ N ≤ 100) indicates the number of blocks in the bottom row. bi (1 ≤ bi ≤ 10000) indicates the number of blocks stacked in the i-th position from the left. bi and bi + 1 are separated by a single space. The total number of blocks is 3 or more.

The number of datasets does not exceed 20.

output

For each data set, the number of sorting operations performed until the triangle is formed is output on one line. However, if a triangle cannot be created or the number of operations exceeds 10000, -1 is output.

Example

Input

6
1 4 1 3 2 4
5
1 2 3 4 5
10
1 1 1 1 1 1 1 1 1 1
9
1 1 1 1 1 1 1 1 1
12
1 4 1 3 2 4 3 3 2 1 2 2
1
5050
3
10000 10000 100
0


Output

24
0
10
-1
48
5049
-1
"""

def min_operations_to_triangular_blocks(N, blst):
    tri_nums = [i * (i + 1) // 2 for i in range(1500)]
    
    if sum(blst) not in tri_nums:
        return -1
    
    end = [i + 1 for i in range(tri_nums.index(sum(blst)))]
    lenb = N
    cnt = 0
    
    while blst != end:
        if cnt > 10000:
            return -1
        blst = [i - 1 for i in blst if i > 1]
        blst.append(lenb)
        lenb = len(blst)
        cnt += 1
    
    return cnt