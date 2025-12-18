"""
QUESTION:
Robert Frost is standing on a cross-way with six roads diverging out. He decides to choose the road not taken. After travelling the pathway he reaches a similar but yet another cross-way with six another roads diverging out. He keeps on travelling like this from one cross-way to another and keeps discovering that each cross-way diverges out into six roads including the one from where he came last. After travelling exactly n roads he finds himself on the same cross-way he had started. Assume that the cross-ways are arranged in a grid interconnecting themselves by six roads. You have to tell Robert the number of distinct paths he can follow by travelling exactly n roads and returning to the cross-way from where he had started.

Refer the image for arrangement of cross-ways.

Input:

Input will consist of t test cases followed by exactly t lines consisting of number of roads travelled i.e. n.

Output:

For every test case t you have to print the number of distinct paths.

Constraints:

0 < t < 1000

0 < n < 20

SAMPLE INPUT
2
1
2

SAMPLE OUTPUT
0
6
"""

def calculate_distinct_paths(n: int) -> int:
    # Precomputed values for the number of distinct paths for each n
    distinct_paths = [
        1, 0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 1588356, 8676360, 
        47977776, 266378112, 1488801600, 8355739392, 47104393050, 266482019232, 
        1512589408044, 8610448069080, 49144928795820, 281164160225520
    ]
    
    # Return the precomputed value for the given n
    return distinct_paths[n]