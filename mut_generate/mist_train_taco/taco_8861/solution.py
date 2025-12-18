"""
QUESTION:
Snuke has four cookies with deliciousness A, B, C, and D. He will choose one or more from those cookies and eat them. Is it possible that the sum of the deliciousness of the eaten cookies is equal to that of the remaining cookies?

-----Constraints-----
 - All values in input are integers.
 - 1 \leq A,B,C,D \leq 10^{8}

-----Input-----
Input is given from Standard Input in the following format:
A B C D

-----Output-----
If it is possible that the sum of the deliciousness of the eaten cookies is equal to that of the remaining cookies, print Yes; otherwise, print No.

-----Sample Input-----
1 3 2 4

-----Sample Output-----
Yes

 - If he eats the cookies with deliciousness 1 and 4, the sum of the deliciousness of the eaten cookies will be equal to that of the remaining cookies.
"""

def can_split_cookies_equally(A, B, C, D):
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    sum1 = 0
                    sum2 = 0
                    if i == 1:
                        sum1 += A
                    else:
                        sum2 += A
                    if j == 1:
                        sum1 += B
                    else:
                        sum2 += B
                    if k == 1:
                        sum1 += C
                    else:
                        sum2 += C
                    if l == 1:
                        sum1 += D
                    else:
                        sum2 += D
                    if sum1 == sum2:
                        return 'Yes'
    return 'No'