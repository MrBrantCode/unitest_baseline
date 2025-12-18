"""
QUESTION:
Mehta is a forever alone and desperate guy. He has a crush on N girls of his society. He wants to impress them all and so he needs to do their task collectively.All the girls give him a number which he stores in an array named A of size N. To do their task, he has to report the number of triplets (i,j,k) in the array A, with  i < j < k such that the triplets have at least one prime digit in common.

Input & Output:
The first line of the input contains an integer N. The next N lines has a number on each, which denote the array A.

You need to print on one line, the number of triples with the condition mentioned in the problem statement.

Constraints:

1 ≤ N ≤  10 ^ 5
0 ≤ A[i] ≤ 10  ^ {18}  for all index i in the array A.

Sample Input:

5
21
22
23
24
25

Sample Output:
10

SAMPLE INPUT
5
21
22
23
24
25

SAMPLE OUTPUT
10

Explanation

In the given sample each i,j,k has one prime digit common that is 2. So, total triplets are 5C3 which is 10.
"""

def count_triplets_with_common_prime_digit(N, A):
    combinations = [0] * 100005

    def combi():
        combinations[3] = 1
        temp = 1
        for i in range(4, 100000):
            temp = (temp * i) // (i - 3)
            combinations[i] = temp

    combi()

    count = [0] * 16

    for number in A:
        c = 0
        ac = number
        while ac > 0:
            digit = ac % 10
            if digit == 2:
                c |= 1
            if digit == 3:
                c |= 2
            if digit == 5:
                c |= 4
            if digit == 7:
                c |= 8
            ac //= 10
        count[c] += 1

    ans = 0
    for i in range(1, 16):
        j = i
        popcount = 0
        while j > 0:
            popcount += 1
            j = j - (j & -j)
        total = 0
        for j in range(i, 16):
            if (j & i) == i:
                total += count[j]

        if popcount % 2 == 0:
            ans -= combinations[total]
        elif popcount % 2 == 1:
            ans += combinations[total]

    return ans