"""
QUESTION:
There are two integers (X and N). You have to make a number in such a way that it contains the first digit and last digit occurring in X^{1 }, X^{2 }, X^{3},  .... X^{N}.
For Example: let's take  X=12 and N=5.
let l is last digit and f is first digit.
12^{1  }= 12, the first digit of 12 is 1(f1) and last digit is 2 (l1).
12^{2} = 144, the first digit of 144 is 1 (f2) and last digit is 4 (l2).
12^{3} = 1728, the first digit of 1728 is 1 (f3) and last digit is 8  (l3).
12^{4} = 20736, the first digit of 20736 is 2 (f4) and last digit is 6 (l4).
12^{5} = 248832, the first digit of 248832 is 2 (f5) and last digit is 2 (l5).
We made a number in the format f1 l1 f2 l2 f3 l3 f4 l4 f5 l5 .
so number becomes 1214182622.
 
Example 1:
Input:
X = 10, N = 2
Output:
1010
Explanation:
10^{1} = 10. So, f1=1 and l1=0
10^{2} = 100. So, f2=1 and l2=0
Therefore, Output is 1010.
Example 2:
Input:
X = 99, N = 1
Output:
99
Explanation:
99^{1} = 99. So, f1=9 and l1=9
Therefore, Output is 99.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function powerGame() which takes 2 Integers X and N as input and returns the answer.
 
Expected Time Complexity: O(N*(Sum of number of digits in X^{1}, X^{2}..., X^{N}))
Expected Auxiliary Space: O(1)
 
Constraints:
10 <= X <= 100
1 <= N <= 8
"""

def power_game(X: int, N: int) -> str:
    result = ''
    for i in range(1, N + 1):
        number = X ** i
        result += str(number)[0] + str(number)[-1]
    return result