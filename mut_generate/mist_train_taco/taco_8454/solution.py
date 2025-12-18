"""
QUESTION:
Jim is doing his discrete maths homework which requires him to repeatedly calculate ^{n}C_{r}(n choose r) for different values of n. Knowing that this is time consuming, he goes to his sister June for help. June,  being a computer science student knows how to convert this into a computer program and generate the answers quickly. She tells him, by storing the lower values of ^{n}C_{r}(n choose r), one can calculate the higher values using a very simple formula. 

If you are June, how will you calculate ^{n}C_{r} values for different values of n?

Since ${}^{n}C_{r}$values will be large you have to calculate them modulo $\mathbf{10^{9}}$.  

Input Format 

The first line contains the number of test cases T. 

T lines follow each containing an integer n. 

Output Format 

For each n output the list of ^{n}C_{0} to ^{n}C_{n} each separated by a single space in a new line. If the number is large, print only the last 9 digits. i.e. modulo 10^{9}

Constraints 

1<=T<=200 

1<=n< 1000

Sample Input

3
2
4
5

Sample Output

1 2 1
1 4 6 4 1
1 5 10 10 5 1

Explanation 

For 2 we can check ^{2}C_{0}  ^{2}C_{1} and ^{2}C_{2} are 1, 2 and 1 respectively. The other inputs' answer follow similar pattern.
"""

def calculate_combinations(n: int) -> list[int]:
    result = []
    temp = 1
    result.append(temp)
    for i in range(1, n + 1):
        temp = temp * (n - i + 1) // i
        result.append(temp % 10**9)
    return result