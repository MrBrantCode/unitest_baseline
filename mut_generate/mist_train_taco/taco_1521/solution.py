"""
QUESTION:
The Gray code (see wikipedia for more details) is a well-known concept.
One of its important properties is that every two adjacent numbers have exactly one different digit in their binary representation.

In this problem, we will give you n non-negative integers in a sequence A[1..n] (0≤A[i]<2^{64}), such that every two adjacent integers have exactly one different digit in their binary representation, similar to the Gray code.

Your task is to check whether there exist 4 numbers A[i1], A[i2], A[i3], A[i4] (1 ≤ i1 < i2 < i3 < i4 ≤ n) out of the given n numbers such that A[i1] xor A[i2] xor A[i3] xor A[i4] = 0. Here xor is a bitwise operation which is same as ^ in C, C++, Java and xor in Pascal.

------ Input ------ 

First line contains one integer n (4≤n≤100000).
Second line contains n space seperated non-negative integers denoting the sequence A.

------ Output ------ 

Output “Yes” (quotes exclusive) if there exist four distinct indices i1, i2, i3, i4 such that A[i1] xor A[i2] xor A[i3] xor A[i4] = 0. Otherwise, output "No" (quotes exclusive) please.

----- Sample Input 1 ------ 
5
1 0 2 3 7
----- Sample Output 1 ------ 
Yes
"""

def check_gray_code_property(n, arr):
    if n > 130:
        return 'Yes'
    else:
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for h in range(k + 1, n):
                        if arr[i] ^ arr[j] ^ arr[k] ^ arr[h] == 0:
                            return 'Yes'
        return 'No'