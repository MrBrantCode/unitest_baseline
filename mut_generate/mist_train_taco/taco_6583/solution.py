"""
QUESTION:
The Aizu Wakamatsu city office decided to lay a hot water pipeline covering the whole area of the city to heat houses. The pipeline starts from some hot springs and connects every district in the city. The pipeline can fork at a hot spring or a district, but no cycle is allowed. The city office wants to minimize the length of pipeline in order to build it at the least possible expense.

Write a program to compute the minimal length of the pipeline. The program reads an input that consists of the following three parts:

Hint

The first line correspondings to the first part: there are three hot springs and five districts. The following three lines are the second part: the distances between a hot spring and a district. For instance, the distance between the first hot spring and the third district is 25. The last four lines are the third part: the distances between two districts. For instance, the distance between the second and the third districts is 9. The second hot spring and the fourth district are not connectable The second and the fifth districts are not connectable, either.



Input

* The first part consists of two positive integers in one line, which represent the number s of hot springs and the number d of districts in the city, respectively.
* The second part consists of s lines: each line contains d non-negative integers. The i-th integer in the j-th line represents the distance between the j-th hot spring and the i-th district if it is non-zero. If zero it means they are not connectable due to an obstacle between them.
* The third part consists of d-1 lines. The i-th line has d - i non-negative integers. The i-th integer in the j-th line represents the distance between the j-th and the (i + j)-th districts if it is non-zero. The meaning of zero is the same as mentioned above.



For the sake of simplicity, you can assume the following:

* The number of hot springs and that of districts do not exceed 50.
* Each distance is no more than 100.
* Each line in the input file contains at most 256 characters.
* Each number is delimited by either whitespace or tab.



The input has several test cases. The input terminate with a line which has two 0. The number of test cases is less than 20.

Output

Output the minimum length of pipeline for each test case.

Example

Input

3 5
12 8 25 19 23
9 13 16 0 17
20 14 16 10 22
17 27 18 16
9 7 0
19 5
21
0 0


Output

38
"""

def calculate_minimal_pipeline_length(s, d, hot_spring_distances, district_distances):
    A = [999 for _ in range(d)]
    
    # Process hot spring distances
    for distances in hot_spring_distances:
        for i in range(d):
            if distances[i] != 0:
                A[i] = min(A[i], distances[i])
    
    # Process district distances
    B = [[999 for _ in range(d)] for _ in range(d)]
    for j in range(d - 1):
        for i in range(d - 1 - j):
            if district_distances[j][i] != 0:
                B[j][i + j + 1] = district_distances[j][i]
                B[i + j + 1][j] = district_distances[j][i]
    
    notevaled = [1 for _ in range(d)]
    ans = 0
    
    for _ in range(d):
        mini = A.index(min(A))
        ans += A[mini]
        notevaled[mini] = 0
        A[mini] = 999
        for x in range(d):
            if notevaled[x]:
                A[x] = min(A[x], B[mini][x])
    
    return ans