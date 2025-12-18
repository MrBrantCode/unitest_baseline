"""
QUESTION:
The Hedgehog likes to give presents to his friend, but no less he likes to receive them.

Having received another present today, the Hedgehog suddenly understood that he has no place to put it as there was no room left on the special shelf in the cupboard. He will have to choose another shelf, but which one should he choose, how large should it be?

In order to get to know this, the Hedgehog asks you to write him a program that will count the estimated number of presents that he will receive during the following N days. Besides, he is guided by the principle: 

  * on each holiday day the Hedgehog will necessarily receive a present, 
  * he receives presents at least every K days (i.e., if he received a present on the i-th day, he will receive the next present no later than on the i + K-th day). 



For the given N and K, as well as the list of holidays among the following N days count the minimal number of presents that could be given to the Hedgehog. The number of today's day is zero, and you should regard today's present as already given (i.e., you shouldn't count it in the answer).

Input

The first line contains integers N and K (1 ≤ N ≤ 365, 1 ≤ K ≤ N).

The second line contains a number C which represents the number of holidays (0 ≤ C ≤ N). Then in the same line follow C numbers ranging from 1 to N which are the numbers of holiday days. The numbers are given in the increasing order, without repeating numbers among them.

Output

Print a single number — the minimal number of presents the Hedgehog will receive over the following N days.

Examples

Input

5 2
1 3


Output

3

Input

10 1
3 6 7 8


Output

10
"""

def calculate_minimal_presents(N: int, K: int, holidays: list) -> int:
    def searchInRange(arr: list, start: int, end: int) -> int:
        for i in range(start, end + 1):
            if i in arr:
                return i
        return -1

    ans = 0
    start = 1
    end = K

    while start <= N:
        day = searchInRange(holidays, start, end)
        if day == -1 and start + K - 1 > N:
            break
        if day == -1:
            start = end + 1
        else:
            start = day + 1
        end = start + K - 1 if start + K - 1 <= N else N
        ans += 1

    return ans