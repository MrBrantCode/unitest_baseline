"""
QUESTION:
Chef has some numbers. His girlfriend Chefina feels good when chef gives her a particular pattern number also called as Armstrong number.
Armstrong number is a number whose sum of its all individual digit raise to the power of the number of digit in that number is equal to that number itself
eg.. 153 = 1^3 + 5^3 + 3^3 (153 is an Armstrong number)
1634 = 1^4 + 6^4 + 3^4 + 4^4 (1634 is an Armstrong number)
As a love guru of chef you have to help chef to find Armstrong numbers Among the numbers which chef has initially so that Chefina feels good

-----Input:-----
First line will contain a positive Integer $T$ which is the number of testcases
Next $T$ lines follows an Integer $N$.

-----Output:-----
For Every n You have to print "FEELS GOOD" without qoutes if it is an armstrong number otherwise Print "FEELS BAD" without quotes

-----Constraints-----
- $1 \leq T \leq 10$
- $2 \leq N \leq 10^6$

-----Sample Input:-----
3
153
11
1634

-----Sample Output:-----
FEELS GOOD
FEELS BAD
FEELS GOOD

-----EXPLANATION:-----
For test case 1 --> 153 = 1^3 + 5^3 + 3^3 (153 is an armstrong number)
"""

def check_armstrong_numbers(test_cases):
    def power(x, y):
        if y == 0:
            return 1
        if y % 2 == 0:
            return power(x, y // 2) * power(x, y // 2)
        return x * power(x, y // 2) * power(x, y // 2)

    def order(x):
        n = 0
        while x != 0:
            n = n + 1
            x = x // 10
        return n

    def isArmstrong(x):
        n = order(x)
        temp = x
        sum1 = 0
        while temp != 0:
            r = temp % 10
            sum1 = sum1 + power(r, n)
            temp = temp // 10
        return sum1 == x

    results = []
    for num in test_cases:
        if isArmstrong(num):
            results.append('FEELS GOOD')
        else:
            results.append('FEELS BAD')
    return results