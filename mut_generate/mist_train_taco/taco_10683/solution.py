"""
QUESTION:
A Lucky number is the largest number made up of only digits 2,3 and 5 such that the count for each digit is divisible by the number obtained by multiplication of remaining two digits. You are provided with the number N and you have to output the lucky number of N digits. If no lucky number exists for the given N output -1.
Example 1:
Input:
N = 4
Output:
-1
Explanation:
There isn't any 4 digit Lucky Number.
Example 2:
Input:
N = 16
Output:
5555553333333333 
Explanation:
There are six '5' and ten '3' in the
number. And also, 2*3=6 and 2*5=10.
There is no 16 digit number greater
which satisfies the conditions.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getLuckyNum() which takes an Integer N as input and returns the answer as a String.
Expected Time Complexity: O(N^{3})
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{3}
"""

def get_lucky_number(N: int) -> str:
    for i in range(N // 6, -1, -1):
        n1 = N - i * 6
        for j in range(n1 // 10, -1, -1):
            n2 = n1 - j * 10
            for k in range(n2 // 15, -1, -1):
                if i * 6 + j * 10 + k * 15 == N:
                    return '5' * (i * 6) + '3' * (j * 10) + '2' * (k * 15)
    return '-1'