"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef has n × n array A of non-negative integers. He wants to divide this array by p-1 horizontal dividers and p-1 vertical dividers into p^{2} blocks such that maximum sum of elements of each block will be the smallest. 

More formally, Chef want to choose p-1 horizontal dividers 0 = h_{0} < h_{1} < ... < h_{p} = n and  p-1 vertical dividers 0 = v_{0} < v_{1} < ... < v_{p} = n to minimize the next value: 

------ Input ------ 

The first line of each test file contains two space-separated integers n and p denoting the size of array A and the number of horizontal and vertical dividers.
Each of next n lines contains n space-separated integers A_{i, 1}, A_{i, 2}, ..., A_{i, n} denoting the i^{th} row of the array A. 

------ Output ------ 

The first line of output should contain p-1 space-separated integers h_{1}, h_{2}, ... h_{p-1} denoting the horizontal dividers.

The second line of output should contain p-1 space-separated integers v_{1}, v_{2}, ... v_{p-1} denoting the vertical dividers.

------ Scoring ------ 

Your score for each test case will be calculated by formula described above. Your goal is to minimize this score.
Your total score for the problem will be the sum of scores on all the test cases.
Your solution will be tested only on 20% of the test files during the contest and will be rejudged against 100% after the end of competition.

------ Constraints ------ 

$2 ≤ p ≤ n ≤ 500 $
$1 ≤ A_{i, j} ≤ 10^{9} $

------ Example ------ 

Input:
4 3
1 1 2 2
2 1 2 2
3 1 4 2
4 4 2 2

Output:
2 3
1 3

------ Explanation ------ 

As you can see at the picture below, this array is divided into p^{2} = 9 blocks by p-1 horizontal(red lines) and p-1 vertical(green lines) dividers. Also there are two vertical (v_{0} = 0 and v_{3} = 4) dividers and two horizontal (h_{0} = 0 and h_{3} = 4) for better understanding of this division.

Your score for this test case will be 6 / (4 / 3)^{2} (there are two blocks with sum of elements 6).
This test case won't be in the test data because n ∉ [450..500]. It just for let you understand how scoring works. Also there are another ways to divide this array into 9 parts. All of them will be accepted, but with different scores. 

------ Test data generation ------ 

There will be 20 test files.
For each test file the number n is chosen from the range [450..500] with equal probability. All elements of A are also chosen randomly. For each test case p will be manually selected.
"""

def minimize_block_sum(n, p, A):
    if p == n:
        horizontal_dividers = list(range(1, n))
        vertical_dividers = list(range(1, n))
        return horizontal_dividers, vertical_dividers
    
    F = [False] * n
    a = 0
    horizontal_dividers = []
    while a != p - 1:
        b = random.randrange(1, n)
        if not F[b]:
            a += 1
            F[b] = True
            horizontal_dividers.append(b)
    
    F = [False] * n
    a = 0
    vertical_dividers = []
    while a != p - 1:
        b = random.randrange(1, n)
        if not F[b]:
            a += 1
            F[b] = True
            vertical_dividers.append(b)
    
    return horizontal_dividers, vertical_dividers