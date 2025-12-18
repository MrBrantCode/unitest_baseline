"""
QUESTION:
There are N coins numbered from 1 to N, all turned tails.N persons flip these coins. When the ith person enters, he flips all coins whose number is divisible by i.Calculate the number of coins that will remain heads after N persons enter and perform fliping operation.
Example 1:
Input:
N=3
Output:
1
Explanation:
initially the configuration is TTT
Person 1 flips all coins divisible
by 1.Now,Configuration is HHH.
Person 2 flips all coins divisible by
2.Now,Configuration is HTH.
Person 3 flips all coins divisible by 
3.Now,finally configuration is HTT.
Thus,Number of heads is 1.
Example 2:
Input:
N=5
Output:
2
Explanation:
Initial configuration=TTTTT
The configuration changes as follows:
TTTTT->HHHHH->HTHTH->HTTTH->
HTTHH->HTTHT.
So, finally number of heads is 2.
Your Task:
You don't need to read input or print anything.Your task is to complete the function numberOfHeads() which takes the number N as input parameter and returns the number of coins that show heads after N persons have performed the flipping peration.
Expected Time Complexity:O(LogN)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{18}
"""

def numberOfHeads(N: int) -> int:
    return int(N ** 0.5)