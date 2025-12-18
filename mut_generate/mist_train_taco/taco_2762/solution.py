"""
QUESTION:
Harold always boasted about his prowess with numbers. So one day Reese challenged him to a problem. He gave Harold two numbers X and Y and asked him to find out the N^th number of the series which began with X numbers of Y’s and the following elements are equal to the sum of the last X numbers in the series. Help Harold find the  N^th number of the series. 

Input:
The first line contains a number T , number of test cases.
The next T lines each contain 3 integers X, Y and N separated by single space.

Output: 
For each test case print the N^th number of the sequence.

Constraints:
1 ≤ T ≤ 10^6
0 < N ≤ 50
0 < X < 50
0 ≤ Y< 3

Problem statement in native language :  http://hck.re/F91Yaz

SAMPLE INPUT
1
3 2 7

SAMPLE OUTPUT
34

Explanation

For X=3,Y=2 the series will be as follow:
2, 2, 2, 6, 10, 18, 34
"""

def find_nth_number_in_series(X, Y, N):
    # Initialize the series with X elements, each equal to Y
    series = [Y] * X
    
    # Generate the series up to the Nth element
    for i in range(N - X):
        # Append the sum of the last X elements to the series
        series.append(sum(series[-X:]))
    
    # Return the Nth element (1-based index, so N-1 in 0-based index)
    return series[N - 1]