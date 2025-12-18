"""
QUESTION:
Dr. Sato, a botanist, invented a number of special fertilizers for seedlings. When you give the fertilizer to the seedlings, the size of the seedlings changes in a blink of an eye. However, it was found that fertilizer has the following side effects.

* The size of the seedlings does not change with the fertilizer given the first time.
* From the second time onward, the seedlings will be affected by the combination of the fertilizer given at that time and the fertilizer given immediately before. Saplings may grow if they have a positive effect, and shrink if they have a negative effect.



As a test, Dr. Sato said that for three types of fertilizers (fertilizers 1, 2, and 3), seedling growth was achieved by combining the fertilizer given at a certain point (this fertilizer) and the fertilizer given immediately before (previous fertilizer). We investigated the degree and created the following "growth table".

The first row of the table on the right is the number of the fertilizer given this time, and the first column is the number of the fertilizer given immediately before. Other numbers indicate the growth rate (ratio of post-growth to pre-growth size) of seedlings due to the combination of the fertilizer given immediately before and the fertilizer given this time. A growth rate of> 1.0 indicates that the sapling grows, and a growth rate of <1.0 indicates that the sapling shrinks. For example, fertilizer 1 followed by fertilizer 2 triples the size of the sapling, but fertilizer 1 followed by fertilizer 3 reduces the size of the sapling in half.

| <image>
--- | ---



If the number of fertilizers given to the seedlings is limited, which fertilizer should be given and in what order to grow the seedlings as large as possible? The "Growth Table" will tell you the answer. As an example, if you give the fertilizers shown in the table above only three times, the seedlings will grow the most if you give them in the order of fertilizer 3 → fertilizer 1 → fertilizer 2 as shown below.

<image>


* The size of the sapling does not change with the first fertilizer (fertilizer 3).
* In the second fertilizer (fertilizer 1), the growth rate of fertilizer 1 after fertilizer 3 is 3.0 from the table, so the size of the seedling is 3.0 times that of the previous time.
* In the third fertilizer (fertilizer 2), the growth rate of fertilizer 2 after fertilizer 1 is 3.0 from the table, so the size of the seedlings is 3.0 times the previous time and 9.0 times the initial 3.0 x 3.0. ..



This time, Dr. Sato examined all the n types of fertilizers he invented and created a "growth table" like the one above, but it turned out to be a very large table, and he decided on the types of fertilizers and the order in which they were given. I am having a hard time.

Therefore, instead of the doctor, I created a program to find the maximum size of the seedling after applying fertilizer m times by inputting the growth value part in the "growth table" of the seedling by combining n kinds of fertilizer. Please give me. However, the size of the first seedling is 1, and the growth rate of the fertilizer given the first time is 1.0 for all fertilizers. Fertilizers are numbered from 1 to n.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by two lines of zeros. Each dataset is given in the following format:


n m
g11 g12 ... g1n
g21 g22 ... g2n
::
gn1 gn2 ... gnn


The first line gives the number of fertilizer types n (2 ≤ n ≤ 100) and the number of fertilizer applications m (1 ≤ m ≤ 100).

The next n lines give the seedling growth gij (0.0 ≤ gij ≤ 10.0, real number) when fertilizer i is followed by fertilizer j.

The number of datasets does not exceed 20.

Output

Outputs the maximum sapling size on one line for each dataset. For the size of the sapling to be output, round off to the second decimal place.

Example

Input

3 3
1.3 3.0 0.5
2.4 2.1 1.0
3.0 0.8 1.2
2 2
1.0 1.0
1.0 1.0
0 0


Output

9.00
1.00
"""

def calculate_max_seedling_size(n, m, growth_table):
    # Initialize the dynamic programming table
    dp = [[0.0 for _ in range(n)] for _ in range(m)]
    
    # The size of the seedling does not change with the first fertilizer
    for i in range(n):
        dp[0][i] = 1.0
    
    # Fill the dynamic programming table
    for k in range(1, m):
        for i in range(n):
            for j in range(n):
                dp[k][j] = max(dp[k][j], dp[k - 1][i] * growth_table[i][j])
    
    # Find the maximum size after m applications
    max_size = max(dp[m - 1])
    
    # Return the maximum size rounded to two decimal places
    return round(max_size, 2)