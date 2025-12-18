"""
QUESTION:
Today Pari and Arya are playing a game called Remainders.

Pari chooses two positive integer x and k, and tells Arya k but not x. Arya have to find the value <image>. There are n ancient numbers c1, c2, ..., cn and Pari has to tell Arya <image> if Arya wants. Given k and the ancient values, tell us if Arya has a winning strategy independent of value of x or not. Formally, is it true that Arya can understand the value <image> for any positive integer x?

Note, that <image> means the remainder of x after dividing it by y.

Input

The first line of the input contains two integers n and k (1 ≤ n, k ≤ 1 000 000) — the number of ancient integers and value k that is chosen by Pari.

The second line contains n integers c1, c2, ..., cn (1 ≤ ci ≤ 1 000 000).

Output

Print "Yes" (without quotes) if Arya has a winning strategy independent of value of x, or "No" (without quotes) otherwise.

Examples

Input

4 5
2 3 5 12


Output

Yes


Input

2 7
2 3


Output

No

Note

In the first sample, Arya can understand <image> because 5 is one of the ancient numbers.

In the second sample, Arya can't be sure what <image> is. For example 1 and 7 have the same remainders after dividing by 2 and 3, but they differ in remainders after dividing by 7.
"""

def has_winning_strategy(n, k, ancient_numbers):
    if k == 1:
        return 'Yes'
    
    # Find the prime factors of k and their powers
    arr1 = []
    temp = k
    for i in range(2, k + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp = temp // i
            arr1.append(i ** cnt)
    
    # Check if all prime factors (or their multiples) are present in ancient_numbers
    mainflag = 0
    for j in arr1:
        flag = 0
        for num in ancient_numbers:
            if num % j == 0:
                flag = 1
                break
        if flag == 0:
            mainflag = 1
            break
    
    if mainflag == 1:
        return 'No'
    else:
        return 'Yes'