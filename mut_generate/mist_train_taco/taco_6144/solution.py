"""
QUESTION:
Chef has an array A consisting of N integers. He also has an intger K.
Chef wants you to find out number of different arrays he can obtain from array A by applying the following operation exactly K times.

- Pick some element in the array and multiply it by -1

As answer could be quite large, print it modulo 109 + 7.

-----Input-----
- The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains two space separated integers N, K as defined above.
- The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

-----Output-----
- For each test case, output a single line containing an integer corresponding to the number of different arrays Chef can get modulo 109 + 7.

-----Constraints-----
- 1 ≤ T ≤ 10
- 1 ≤ N, K ≤ 105
- -106 ≤ Ai ≤ 106

-----Subtasks-----
- Subtask #1 (10 points) : N, K ≤ 10
- Subtask #2 (30 points) : N, K ≤ 100
- Subtask #3 (60 points) : N, K ≤ 105

-----Example-----
Input:
3
1 3
100
3 1
1 2 1
3 2
1 2 1

Output:
1
3
4

-----Explanation-----
Example case 1.
Chef has only one element and must apply the operation 3 times to it. After applying the operations, he will end up with -100. That is the only array he will get.

Example case 2.
Chef can apply operation to one of three elements. So, he can obtain three different arrays.

Example case 3.
Note that other than applying operation to positions (1, 2), (1, 3), (2, 3), Chef can also apply the operation twice on some element and get the original.

In summary, Chef can get following four arrays.

[1, 2, 1]
[-1, -2, 1]
[-1, 2, -1]
[1, -2, -1]
"""

def count_different_arrays(N, K, A):
    fact = [1]
    for i in range(1, 100001):
        fact.append(i * fact[i - 1] % 1000000007)

    def power(a, b, p):
        x = 1
        y = a
        while b > 0:
            if b % 2 == 1:
                x = x * y
                if x > p:
                    x = x % p
            y = y * y
            if y > p:
                y = y % p
            b = b // 2
        return x

    def inverse(N, p):
        return power(N, p - 2, p)

    def combination(N, R, p):
        return fact[N] * (inverse(fact[R], p) * inverse(fact[N - R], p) % p) % p

    numZ = 0
    answer = 0
    p = 1000000007

    for j in range(len(A)):
        if A[j] == 0:
            numZ += 1

    N = N - numZ

    if numZ > 0:
        if N > K:
            temp = K
            while temp >= 0:
                answer = (answer + combination(N, temp, p)) % p
                temp -= 1
        else:
            temp = N
            while temp >= 0:
                answer = (answer + combination(N, temp, p)) % p
                temp -= 1
    elif N > K:
        temp = K
        while temp >= 0:
            answer = (answer + combination(N, temp, p)) % p
            temp -= 2
    else:
        temp = N
        while temp >= 0:
            answer = (answer + combination(N, temp, p)) % p
            temp -= 2

    return answer