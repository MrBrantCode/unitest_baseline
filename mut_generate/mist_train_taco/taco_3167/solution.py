"""
QUESTION:
Sherlock is stuck while solving a problem: Given an array $A=\{a_1,a_2,\cdots,a_N\}$, he wants to know if there exists a subset $\mbox{B}$ of this array which follows these statements:

$\mbox{B}$ is a non-empty subset.
There exists no integer $x(x>1)$ which divides all elements of $\mbox{B}$.
There are no elements of $\mbox{B}$ which are equal to another.

Input Format

The first line of input contains an integer, $\mathbf{T}$, representing the number of test cases. Then $\mathbf{T}$ test cases follow. 

Each test case consists of two lines. The first line contains an integer, $N$, representing the size of array $\mbox{A}$. In the second line there are $N$ space-separated integers, $a_1,a_2,\ldots,a_n$, representing the elements of array $\mbox{A}$.

Constraints 

$1\leq T\leq10$ 

$1\leq N\leq100$ 

$1\leq a_i\leq10^5\:\forall1\leq i\leq N$   

Output Format

Print YES if such a subset exists; otherwise, print NO.

Sample Input
3
3
1 2 3
2
2 4
3
5 5 5

Sample Output
YES
NO
NO

Explanation

In the first test case, $\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\}\ \text{and}\ \{1,2,3\}$ are all the possible non-empty subsets, of which the first and the last four satisfy the given condition.

For the second test case, all possible subsets are $\{2\},\{4\},\{2,4\}$. For all of these subsets, $x=2$ divides each element. Therefore, no non-empty subset exists which satisfies the given condition.

For the third test case, the following subsets exist: $\mbox{S}$_{1}$=\{5\},S$_{2}$=\{5,5\},\:\text{and}\:S$_{3}$=\{5,5,5\}$. 
Because the single element in the first subset is divisible by $5$ and the other two subsets have elements that are equal to another, there is no subset that satisfies every condition.
"""

def has_valid_subset(arr):
    def gcd(a, b):
        while b:
            a %= b
            (a, b) = (b, a)
        return a
    
    if not arr:
        return False
    
    res = arr[0]
    for i in range(1, len(arr)):
        res = gcd(res, arr[i])
    
    return res == 1