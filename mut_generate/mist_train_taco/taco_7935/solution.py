"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Sereja likes arithmetic progressions a lot. An infinite arithmetic progression (a, r) is determined by its initial term and difference of consecutive terms, denoted by a, r respectively.

He defines mutual attraction of some array A of size N with an infinite arithmetic progression (a, r), as |A_{1} - a| + |A_{2} - (a + r)| + .. + |A_{i} - (a + r * (i - 1)| + .. + |A_{N} - (a + r * (N - 1)|, where |x| denotes absolute value of x.

He has an array A of size N with him. He wants to find some infinite arithmetic progression with which its mutual attraction is minimized. Also, he is allowed to perform following operations on this array. 

Swap operation: Take any two indices i, j of the array A, and swap A_{i}, A_{j}
Delete operation: Delete some element of the array A. Please note that after the deletion, the indices of array are not re-enumerated or re-adjusted.

So, you have to help Sereja in deciding how these operations should be performed on A and also in finding the parameters (a, r) of the infinite arithmetic progression. Note that Sereja can perform at max K swap operations and D delete operations.

------ Scoring ------ 

For each test file, there will be a single test case.
Your score for a single test file will be mutual attraction of the modified array A and the infinite arithmetic progression provided by you, divided by the initial size of array N. Your target is to minimize the score.

------ Input ------ 

There will be a single test case.
First line of input contains three space separated integers N, K, D.
Next line contains N space separated integers denoting array A.

------ Output ------ 

You can print at max K + D + 2 lines.
In the first line, print two space separated real numbers denoting a, r, satisfying the constraints as mentioned in constraints section.
Then, you can print at max K + D lines, with each line having one of the following two formats.

Swap operation = 1 i j: i.e., 1 followed by the indices that you want to swap.
Delete operation = 2 i: i.e., 2 followed by index you want to delete.

Please end your output by printing -1 in a separate line.

Please note that you should ensure that indices that you are trying to swap or delete actually exist, otherwise you will get a WA verdict. The indices should be 1 based. Also note that after the deletion operation, the indices are not re-enumerated. Please see example input/output section for more details. Also note that if you make more than K swaps or more than D deletions, you will get a WA verdict.

------ Constraints ------ 

$-10^{9} ≤ A_{i} ≤ 10^{9}$
$-10^{10} ≤ a, r ≤ 10^{10}$

------ Example ------ 

Input:
3 1 1
1 2 3

Output:
0 1
2 1
1 2 3
-1

------ Explanation ------ 

In this case, the array A is [1, 2, 3]. Sereja can perform at max one swap and at max one deletion operation.
He first delete index 1, the new array becomes [1, 2, 3], in which index 1 is deleted.
After that he makes a swap operation between index 2 and 3. So, at the end the array will be [1 3 2], where the index 1 is deleted.
In the end, the non-deleted elements in the array will be [3, 2]. The Mutual attraction of this array with infinite arithmetic progression (0, 1) will be |3 - 0| + |2 - 1| = 4. So, he will get a score of 4 / 3 = 1.3333. 

------ Test Generation Scheme ------ 

There are total 20 test files and four groups of test files, i.e. 5 test files per group. During the contest, score of your program will be decided by only 20% of the files, i.e. by 4 files, each from one group. However verdict of your program will be based on all the test files, i.e. in order to get an AC, your program should work correctly on all the test files.

$Group 1: N = 100, K = 20, D = 10$
$Group 2: N = 10^{3}, K = 300, D = 100$
$Group 3: N = 10^{4}, K = D = 2000$
$Group 4: N = 10^{5}, K = D = 30000$

The array A will be generated uniformly randomly.
"""

def minimize_mutual_attraction(N, K, D, A):
    # Sort the array in descending order
    A.sort(reverse=True)
    
    # Initialize the parameters for the arithmetic progression
    a = 0
    r = 1
    
    # List to store the operations performed
    operations = []
    
    # Perform delete operations
    ind = 1
    while D > 0:
        operations.append(('2', ind))
        A[ind - 1] = '@'  # Mark the element as deleted
        ind += 1
        D -= 1
    
    # Perform swap operations
    i = 0
    while K > 0:
        if A[i] != '@':
            operations.append(('1', i + 1, i + 2))
            A[i], A[i + 1] = A[i + 1], A[i]
            K -= 1
        i += 1
    
    # Return the parameters and operations
    return a, r, operations