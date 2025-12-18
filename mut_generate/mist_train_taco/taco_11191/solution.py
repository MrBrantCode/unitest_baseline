"""
QUESTION:
Little Petya likes numbers a lot. Recently his mother has presented him a collection of n non-negative integers. There's only one thing Petya likes more than numbers: playing with little Masha. He immediately decided to give a part of his new collection to her. To make the game even more interesting, Petya decided to give Masha such collection of numbers for which the following conditions fulfill:

  * Let's introduce x1 to denote the xor of all numbers Petya has got left; and let's introduce x2 to denote the xor of all numbers he gave to Masha. Value (x1 + x2) must be as large as possible. 
  * If there are multiple ways to divide the collection so that the previous condition fulfilled, then Petya minimizes the value x1. 



The xor operation is a bitwise excluding "OR", that is denoted as "xor" in the Pascal language and "^" in C/C++/Java.

Help Petya divide the collection as described above. If there are multiple suitable ways to divide it, find any of them. Please note that after Petya gives a part of his numbers to Masha, he may have no numbers left. The reverse situation is also possible, when Petya gives nothing to Masha. In both cases we must assume that the xor of an empty set of numbers equals 0.

Input

The first line contains integer n (1 ≤ n ≤ 105), showing how many numbers Petya's mother gave him. The second line contains the actual space-separated numbers. They are all integer, non-negative and do not exceed 1018.

Output

Print n space-separated integers, the i-th of them should equal either 1, if Petya keeps the number that follows i-th in his collection, or it should equal 2, if Petya gives the corresponding number to Masha. The numbers are indexed in the order in which they are given in the input.

Examples

Input

6
1 2 3 4 5 6


Output

2 2 2 2 2 2


Input

3
1000000000000 1000000000000 1000000000000


Output

2 2 2


Input

8
1 1 2 2 3 3 4 4


Output

1 2 1 2 2 2 1 2
"""

def divide_collection(n, arr):
    base = [-1] * 60
    how = [-1] * 60
    who = [-1] * 60
    
    x = 0
    for a in arr:
        x ^= a
    
    mapper = [-1] * 60
    ind = 59
    ind_start = bin(x).count('1') - 1
    
    for bit in reversed(range(60)):
        if 1 << bit & x:
            mapper[bit] = ind_start
            ind_start -= 1
        else:
            mapper[bit] = ind
            ind -= 1
    
    for i in range(len(arr)):
        temp = 0
        for bit in range(60):
            if 1 << bit & arr[i]:
                temp ^= 1 << mapper[bit]
        arr[i] = temp
    
    for i in range(n):
        x = arr[i]
        temp_how = 0
        while x > 0:
            b = x.bit_length() - 1
            if who[b] != -1:
                temp_how ^= how[b]
                x = x ^ base[b]
            else:
                who[b] = i
                base[b] = x
                how[b] = temp_how | 1 << b
                break
    
    x = 0
    temp = 0
    for bit in reversed(range(60)):
        if x & 1 << bit == 0 and who[bit] != -1:
            x ^= base[bit]
            temp ^= how[bit]
    
    result = [1] * n
    for j in range(60):
        if temp & 1 << j:
            result[who[j]] = 2
    
    return result