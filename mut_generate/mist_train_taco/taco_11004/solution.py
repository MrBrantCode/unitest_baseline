"""
QUESTION:
Vasya learned about integer subtraction in school. He is still not very good at it, so he is only able to subtract any single digit number from any other number (which is not necessarily single digit).
For practice, Vasya chose a positive integer n$n$ and wrote it on the first line in his notepad. After that, on the second line he wrote the result of subtraction of the first digit of n$n$ from itself. For example, if n=968$n = 968$, then the second line would contain 968−9=959$968 - 9 = 959$, while with n=5$n = 5$ the second number would be 5−5=0$5 - 5 = 0$. If the second number was still positive, then Vasya would write the result of the same operation on the following line, and so on. For example, if n=91$n = 91$, then the sequence of numbers Vasya would write starts as follows: 91,82,74,67,61,55,50,…$91, 82, 74, 67, 61, 55, 50, \ldots$. One can see that any such sequence eventually terminates with the number 0$0$.
Since then, Vasya lost his notepad. However, he remembered the total number k$k$ of integers he wrote down (including the first number n$n$ and the final number 0$0$). What was the largest possible value of n$n$ Vasya could have started with?

-----Input:-----
The first line contains T$T$ , number of test cases per file.
The only line in each testcase contains a single integer k−$k-$ the total number of integers in Vasya's notepad (2≤k≤1012$2 \leq k \leq 10^{12}$).

-----Output:-----
Print a single integer−$-$ the largest possible value of the starting number n$n$. It is guaranteed that at least one such number n$n$ exists, and the largest possible value is finite.

-----Constraints-----
- 1≤T≤34$1 \leq  T \leq 34 $
- 2≤k≤1012$2 \leq k \leq 10^{12}$

-----Sample Input-----
3
2
3
100

-----Sample Output:-----
9
10
170
"""

def find_largest_starting_number(k):
    if k == 1:
        return 0
    elif k == 2:
        return 9
    elif k == 3:
        return 10
    
    def get_steps(num):
        if num < 10:
            return 2
        last = int(str(num)[0])
        rem = int(str(num)[1:])
        steps = 2
        p = len(str(num)) - 1
        while True:
            steps += rem // last + 1
            rem = rem % last
            if last > 0:
                rem = rem + 10 ** p - last
            last = last - 1
            if last == 0:
                p = p - 1
                last = 9
                if len(str(rem)) == 1:
                    rem = 0
                else:
                    rem = int(str(rem)[1:])
            if rem == 0:
                break
        return steps
    
    (low, high, ans) = (0, 10 ** 18, 0)
    while low <= high:
        mid = (low + high) // 2
        temp = get_steps(mid)
        if int(temp) == k:
            ans = max(ans, mid)
            low = mid + 1
        elif temp < k:
            low = mid + 1
        else:
            high = mid - 1
    
    return ans