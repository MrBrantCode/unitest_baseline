"""
QUESTION:
You are a product engineer and would like to improve the quality of duct tapes that your company manufactures. An entire tape can be represented as a single row of N cells. Each cell has its Stickiness factor, which stands for its ability to stick to an object. We say that a tape is a good quality product, if and only if the total sum of Stickiness factors of grid cells in any of its subarray of size K is at least D.

To make a quality product, consider an augment operation in which you can choose any subarray of size at most K  and a real number (say R), and multiply Stickiness factor of all its cells by R. For each augment operation, the subarray and the value of R can be chosen arbitrarily. However, the size of chosen subarray for augmentation can be at most K, as mentioned before. 

Your task is to calculate the minimum number of augment operations needed to be performed in order to transform the given tape to a good quality product.

INPUT

The first line contains three space separated integers N, K and D, as described above. The next line contains N space separated integers, i^th of which (denoted by Ai) denotes the Stickiness factor of i^th cell.

OUTPUT

Output in single line, an integer, which denotes the minimum number of augment operations needed to be performed in order to transform the tape to a good quality product. In case, if it is impossible to achieve, print -1 instead.

CONSTRAINTS

1 ≤ N, D ≤ 10^5
1 ≤ K ≤ N
0 ≤ Ai ≤ 10^5

SAMPLE INPUT
3 2 4
1 1 1 

SAMPLE OUTPUT
1

Explanation

We can multiply the second element by 3. Now the tape becomes: 1 3 1. 

Any subarray of size 2 has now sum = 4, which satisfies the required condition. We used 1 augment operation, hence the answer is 1.
"""

def min_augment_operations(N, K, D, arr):
    csum = sum(arr[:K - 1])
    for x in range(K - 1, N):
        csum += arr[x]
        if csum == 0:
            return -1
        csum -= arr[x - (K - 1)]
    
    count, lastnz, pick = 0, -1, [0] * N
    csum = 0
    x = 0
    while x < N:
        if arr[x]:
            lastnz = x
        csum += arr[x]
        pick[x] = 1
        if x < K - 1:
            x += 1
            continue
        if pick[x - K]:
            csum -= arr[x - K]
        if csum < D:
            count += 1
            csum = 0
            pick[x] = 0
            x = lastnz + 2 * K - 1
            for y in range(lastnz + K, min(lastnz + 2 * K - 1, N)):
                if arr[y]:
                    lastnz = y
                pick[y] = 1
                csum += arr[y]
        else:
            x += 1
    
    return count