"""
QUESTION:
Chef has created a special dividing machine that supports the below given operations on an array of positive integers.
There are two operations that Chef implemented on the machine.
Type 0 Operation

Update(L,R):
	for i = L to R:
		a[i] = a[i] / LeastPrimeDivisor(a[i])

Type 1 Operation

Get(L,R):
	result = 1
	for i = L to R:
		result = max(result, LeastPrimeDivisor(a[i]))
	return result;

The function LeastPrimeDivisor(x) finds the smallest prime divisor of a number. If the number does not have any prime divisors, then it returns 1.
Chef has provided you an array of size N, on which you have to apply M operations using the special machine. Each operation will be one of the above given two types. Your task is to implement the special dividing machine operations designed by Chef. Chef finds this task quite easy using his machine, do you too?

-----Input-----

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. 
The first line of each test case contains two space-separated integers N, M, denoting the size of array A and the number of queries correspondingly.

The second line of each test case contains N space-separated integers A1, A2, ..., AN denoting the initial array for dividing machine.
Each of following M lines contain three space-separated integers  type, L, R - the type of operation (0 - Update operation, 1 - Get operation), and the arguments of function, respectively

-----Output-----
For each test case, output answer of each query of type 1 (Get query) separated by space. Each test case from the same file should start from the new line.

-----Constraints-----
- 1 ≤ T ≤ 100
- 1 ≤ Ai ≤ 106
- 1 ≤ L ≤ R ≤ N
- 0 ≤ type ≤ 1
-  Sum of M over all test cases in a single test file does not exceed 106

-----Subtasks-----
Subtask #1: (10 points) 
- 1 ≤ N, M ≤ 103

Subtask #2: (25 points)
- 1 ≤ N, M ≤ 105
-  Ai is a prime number. 

Subtask #3: (65 points)
- 1 ≤ N, M ≤ 105

-----Example-----
Input:
2
6 7
2 5 8 10 3 44
1 2 6
0 2 3
1 2 6
0 4 6
1 1 6
0 1 6
1 4 6
2 2
1 3
0 2 2
1 1 2
Output:
5 3 5 11
1

-----Explanation-----
Example case 1.The states of array A after each Update-operation:
A: = [2 1 4 10 3 44]
A: = [2 1 4 5 1 22]
A: = [1 1 2 1 1 11]
"""

import math

def least_prime_divisor(x):
    """Helper function to find the least prime divisor of x."""
    if x % 2 == 0:
        return 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return i
    return x

def process_operations(arr, operations):
    """
    Process the given operations on the array and return the results of Get operations.

    Parameters:
    - arr: List of integers representing the initial array.
    - operations: List of tuples (type, L, R) where type is 0 for Update and 1 for Get,
                  L and R are the indices for the operation.

    Returns:
    - List of results for each Get operation.
    """
    n = len(arr)
    Matrix = []
    factors = [0] * n
    index = [0] * n
    results = []

    # Precompute the least prime divisors for each element in the array
    for r in range(n):
        li = []
        x = arr[r]
        while x != 1:
            lpd = least_prime_divisor(x)
            while x % lpd == 0:
                x //= lpd
                li.append(lpd)
                factors[r] += 1
        Matrix.append(li)

    # Process each operation
    for opr in operations:
        type_op, L, R = opr
        L -= 1  # Convert to 0-based index
        R -= 1  # Convert to 0-based index

        if type_op == 0:
            for ran in range(L, R + 1):
                if index[ran] < factors[ran]:
                    index[ran] += 1
        elif type_op == 1:
            result = 1
            for ran in range(L, R + 1):
                if index[ran] < factors[ran]:
                    result = max(result, Matrix[ran][index[ran]])
            results.append(result)

    return results