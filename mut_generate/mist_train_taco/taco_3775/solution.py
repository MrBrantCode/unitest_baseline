"""
QUESTION:
In the Kingdom of AtCoder, only banknotes are used as currency. There are 10^{100}+1 kinds of banknotes, with the values of 1, 10, 10^2, 10^3, \dots, 10^{(10^{100})}. You have come shopping at a mall and are now buying a takoyaki machine with a value of N. (Takoyaki is the name of a Japanese snack.)
To make the payment, you will choose some amount of money which is at least N and give it to the clerk. Then, the clerk gives you back the change, which is the amount of money you give minus N.
What will be the minimum possible number of total banknotes used by you and the clerk, when both choose the combination of banknotes to minimize this count?
Assume that you have sufficient numbers of banknotes, and so does the clerk.

-----Constraints-----
 - N is an integer between 1 and 10^{1,000,000} (inclusive).

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the minimum possible number of total banknotes used by you and the clerk.

-----Sample Input-----
36

-----Sample Output-----
8

If you give four banknotes of value 10 each, and the clerk gives you back four banknotes of value 1 each, a total of eight banknotes are used.
The payment cannot be made with less than eight banknotes in total, so the answer is 8.
"""

def minimum_banknotes(N: str) -> int:
    L = len(N)
    ans = [[0 for _ in range(2)] for _ in range(L)]
    k = int(N[L - 1])
    ans[0][0] = k
    ans[0][1] = 10 - k
    
    if L > 1:
        for i in range(1, L):
            k = int(N[L - 1 - i])
            ans[i][0] = min(ans[i - 1][0] + k, ans[i - 1][1] + k + 1)
            ans[i][1] = min(ans[i - 1][0] + 10 - k, ans[i - 1][1] + 10 - k - 1)
    
    return min(ans[L - 1][0], ans[L - 1][1] + 1)